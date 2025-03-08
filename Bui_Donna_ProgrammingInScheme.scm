; Programming in Scheme - Donna Bui - 5/12/2023 - Professor Henry Estrada's COMSC 078
; This program contains a cube function, a sum-integers function which calculates the sum of all numbers between two numbers, 
; a sum-cube functions which calculates the sum of all cubes of a range of numbers, a pi-sum function that slowly converges to pi, 
; and a higher order function that accepts a function and calculates the sum between a range.

(define (cube x) 
    (* x x x)
)
(cube 4) ; Returns 64. 4*4*4 = 64


(define (sum-integers a b) ; Defines the sum-integers function
    (if (> a b)
        0 ; If a > b, return 0
        (+ a (sum-integers (+ a 1) b) ; Recursively call the sum-integers method  
        ) ; Equivalent to (a += sum_integers(a+1, b)) in python, recursively adds the number after it until b is reached
    )
)
(sum-integers 1 3) ; Returns 6. 1+2+3 = 6


(define (sum-cubes a b) ; Defines the sum-cubes function. 
    ; Pretty much the same thing as sum-integers, but instead of using 'a' as the starting variable, this uses cube(a)
    (if (> a b)
        0 
        (+ (cube a) (sum-cubes (+ a 1) b) ; Equivalent to (a += (cube(a) + (sum_cubes(a+1), b))) in python  
        ) 
    )
)
(sum-cubes 1 3) ; Returns 36. 1 + (2 * 2 * 2) + (3 * 3 * 3) = 1 + 8 + 27 = 36


(define (pi-sum n) ; Defines the pi-sum function.
    (define (sum total k) ; Defines another function that accepts two parameters, equivalent to sum(total, k) in Python
        (if (> k n) 
            total ; If k > n, return total
            (sum (+ total (/ 8.0 (* (- (* 4 k) 3) (- (* 4 k) 1)))) (+ k 1)) ; Recursively alls itself until k > n.  
            ; This is equivalent to return sum((total + 8 / ((4*k-3) * (4*k-1))), k + 1) in Python. 
        )
    ) 
    (sum 0 1) ; Call the sum for the first time, with total = 0 and k = 1
)
(pi-sum 3) ; Returns 2.976046176046176, which is the equivalent of (8/3)+(8/35)+(8/99) 
(pi-sum 1000) ; It works! Returned value: 3.141092653621038


(define (summation f a b) ; Equivalent to summation(f, lower, upper) 
    (if (> a b) 
        0 ; If a > b, return the total
        (+ (f a) (summation f (+ a 1) b)) ; Recursively calls itself until a > b. Equivalent to return f(a) + summation (f(a+1), b) in Python
    )
)
(summation cube 1 3) ; Returns 36, same as sum-cubes.

