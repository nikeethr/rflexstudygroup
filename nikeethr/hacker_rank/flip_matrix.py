def find_max_first_quadrant_sum(A):
    """
        Given a 2N by 2N matrix A where first quadrant = A(i,j) i,j in [1,N]

        Suppose:
        1. Any (i,j) can only translate to the following other positions (2N-i,j), (i,2N-j),
           (2N-i,2N-j). To see this consider the following:

           Flipping is an involutory function, i.e. f(f(x)) = x. We have two flip functions f() for
           rows and g() for columns. So the possible translations are g(x), f(x) and g(f(x)) =
           f(g(x)).

        2. Any (i,j) in the first quadrant can be moved independently without affecting any other
           element in the first quadrant. To see this consider the following:

           If we want to move (i,2N-j) to (i,j) we will have to flip row i but this will change the
           entire row. However, if we flip every other column (in the first quadrant) except column
           j then these columns would not be affected by flipping row i. Furthermore, only (i,j) in
           column j will be affected by flipping row i.

           Now, we flip row i and flip back every other column except j we would have returned every
           column back to its original state in the first quadrant. The only element that was
           changed would be (i,j)

           We can apply a similar reasoning for (2N-i,j) -> (i,j)

           For (2N-i,2N-j) -> (i,j) we can first flip it to (2N-i,j) or (i,2N-j) without affecting
           the first quadrant and repeat the above reasoning.

        Then:
        Using 1. we know that the potential max value of each (i,j) in the first quadrant is given
        by max(A(i,j), A(2N-i,j), A(i,2N-j), A(2N-i,2N-j)).

        Using 2. we know that any of the elements (2N-i,j), (i,2N-j), (2N-i,2N-j) can be moved to
        (i,j) independent of of any other element in the first quadrant.

        Thus, the max sum of the first quadrant is simply
        sum(max(A(i,j), A(2N-i), A(i,2N-j), A(2N-i, 2N-j))) for all i,j in [1,N]
    """

    if len(A) == 0 or len(A) % 2 != 0 or len(A) != len(A[0]):
        raise("Invalid matrix, must be 2N x 2N")

    N = len(A) // 2
    tot = 0

    for i in range(N):
        for j in range(N):
            tot += max((A[i][j], A[i][2*N-j-1], A[2*N-i-1][j], A[2*N-i-1][2*N-j-1]))

    return tot

if __name__ == '__main__':
    q = int(input())
    for i in range(q):
        n = int(input())
        A = []
        for j in range(2*n):
            r = [int(x) for x in input().strip().split(' ')]
            A.append(r)
        print(find_max_first_quadrant_sum(A))
