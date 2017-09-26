library(dplyr)
library(maps)
library(mapdata)
library(ggplot2)

# Plan

# initial visualisation
# - get us map data [X]
# - draw statelines [X]
# - draw nyc []
# - zoom into nyc []
# - draw county lines []
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

ny_5nn <- states[states$region %in% regions_nn$region,]

p <- ggplot(data = states) +
     geom_polygon(aes(x=long, y=lat, group=group), fill=NA, color='black') +
     geom_polygon(data=ny_5nn,aes(x=long, y=lat, group=group, color=region), fill=NA) +
     geom_polygon(data=ny,aes(x=long, y=lat, group=group, fill=subregion)) +
     coord_fixed(1.3)

# todo:
# - use ggmap to get better plot of new york
# - attach plots of neighbouring areas to map (+ labels)
# - for each point in taxi data check wich state (sufficient to find 4 points encompassing the
# location). Think of "cross" if something is contained if we draw a cross it must touch all
# boundaries. In this case find one point above,below,left and right
