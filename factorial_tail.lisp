;; Name: Kushal Kothari
;; University ID: N15066497

;; defining tail recursive factorial function
(defun factorial_tail(input_value &optional (acc 1))
  (if (<= input_value 1)
      acc
      (factorial_tail (- input_value 1) (* acc input_value))))

;; Print the factorial using tail recursive function
(format t "Tail Recursion Factorial of 4: ~a~%" (factorial_tail 4))
