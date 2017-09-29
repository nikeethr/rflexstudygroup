library(dplyr)
library(maps)
library(mapdata)
library(ggplot2)
library(ggmap)
library(ggthemes)
library(rgdal)
library(httr)
library(dplyr)

# Plan

# initial visualisation
# - get us map data [X]
# - draw statelines [X]
# - draw nyc [X]
# - zoom into nyc [X]
# - draw county lines [X]
# - for each taxi long/lat get which state/city it was from (whether or not it was within nyc)

# prepare data
# - define hbin and vbin []
# - get frequency of pickup/dropoff by vendor []
# - make dataframe of long,lat rect vs n() []
# - do gradient plot on dataframe (for one vendor and pickup) []
# - expand to 4 plots []

# repeat 'prepare data' for various months []
# repeat 'prepare data' for various days of the week []

# get top 10 most frequent pickup->dropoffs []

# split pickup dropoffs by short/long duration []
# split pickup dropoffs by short/long distance []

# split up plots somehow for each NYC "area"


# Playing around with names

us <- map_data('usa')
states <- map_data('state')
ny <- states[states$region == 'new york',]

# nearest neightbours of NY (note dodgy calc using lat-long)
k = 8 
state_avg <- states %>% group_by(region) %>% summarise(long_avg = mean(long), lat_avg = mean(lat))
lat_long_ny <- state_avg[state_avg$region == 'new york', c('lat_avg', 'long_avg')]
regions_nn <- state_avg %>% 
    rowwise() %>% 
    mutate(dst_to_ny = sqrt((lat_avg - lat_long_ny$lat_avg)^2 + 
                            (long_avg - lat_long_ny$long_avg)^2)) %>%
    arrange(dst_to_ny) %>%
    slice(1:k)

ny_knn <- states[states$region %in% regions_nn$region,]

p <- ggplot(data = states) +
     geom_polygon(aes(x=long, y=lat, group=group), fill=NA, color='black') +
     geom_polygon(data=ny_knn,aes(x=long, y=lat, group=group, color=region), fill=NA) +
     geom_polygon(data=ny,aes(x=long, y=lat, group=group, fill=subregion)) +
     coord_fixed(1.3)


# Gather data
setwd("D:\\Projects\\Redflex\\Study Group\\rflexstudygroup\\nikeethr\\kaggle\\nyc_taxi_trip_duration\\data")
train <- read.csv("train.csv", nrow=50000)

nyc <- get_map("New York City", maptype = "toner-lines")
nyc_map <- ggmap(nyc)

# https://rpubs.com/jhofman/nycmaps
r <- GET('http://data.beta.nyc//dataset/0ff93d2d-90ba-457c-9f7e-39e47bf2ac5f/resource/35dd04fb-81b3-479b-a074-a27a37888ce7/download/d085e2f8d0b54d4590b1e7d1f35594c1pediacitiesnycneighborhoods.geojson')
nyc_neighborhoods <- readOGR(content(r,'text'), 'OGRGeoJSON', verbose = F)

nyc_neighborhoods_df <- fortify(nyc_neighborhoods)


# http://www.siam.org/meetings/sdm10/tutorial3.pdf [slide 19]
classifyOutliers <- function(df, cols) {
    mat <- as.matrix(df[,cols])
    v <- var(mat)
    v_inv = solve(v)
    m <- colMeans(mat)

    mahDist <- function(x, v_inv, m) {
        t(x - m) %*% v_inv %*% (x - m)
    }

    mdist <- apply(mat, 1, mahDist, v_inv = v_inv, m = m)
    # 97.5 percentile
    df$outlier = F
    df$mdist = mdist
    df[mdist > qchisq(0.999, 2),"outlier"] = T
    df
}

train <- classifyOutliers(train, c("pickup_latitude", "pickup_longitude"))

p <- nyc_map + 
    stat_density2d(aes(x=pickup_longitude,
                   y=pickup_latitude,
                   fill = ..level..), 
                   alpha = .75, data=train, geom="polygon") +
    geom_path(data=nyc_neighborhoods_df,
                 aes(x=long, y=lat, group=group),
                 color="red",
                 alpha=0.5) +
    geom_point(data=train[train$outlier,],
               aes(x=pickup_longitude, y=pickup_latitude, size=mdist),
               colour='magenta')
# todo:
# - use ggmap to get better plot of new york
# - attach plots of neighbouring areas to map (+ labels)
# - for each point in taxi data check wich state (sufficient to find 4 points encompassing the
# location). Think of "cross" if something is contained if we draw a cross it must touch all
# boundaries. In this case find one point above,below,left and right
