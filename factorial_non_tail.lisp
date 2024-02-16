;; Name: Kushal Kothari
;; University ID: N15066497

;; Calculating the factorial of N.
(defun factorial_non_tail(input_value)
  (if (not (> input_value 1))
      1
      (* input_value (factorial_non_tail(- input_value 1)))))

;; Printing the result
(format t "Non tail recursive factorial of 99999: ~a~%" (factorial_non_tail 99999))
