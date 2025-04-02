; ; Rule: If X develops Y and Y uses Z, then X uses Z
; (= (tech-stack $company)
;    (match &self
;      (, (develops $company $product)
;         (uses $product $tech))
;      $tech))

; ; FAQ Query Rule
; (= (find-faq $question)
;    (match &self 
;      (FAQ $question $answer) 
;      $answer))
; Now includes the agent logic directly
; Add this to force evaluation
; Rule 1: Basic FAQ lookup
(= (find-faq $question)
   (match &self (FAQ $question $answer) $answer))

; Rule 2: Technology inference
(= (get-tech-stack $product)
   (match &self (uses $product $tech) $tech))

; Rule 3: Enhanced response generator
(= (generate-response $question)
   (let* (($direct-answer (find-faq $question))
          ($related-tech (if (== $direct-answer (empty))
                           (match &self 
                             (FAQ $q $a) 
                             (get-tech-stack $product-when-matched))
                           (empty))))
     (if (== $direct-answer (empty))
         "I don't know, but here are related technologies: $related-tech"
         $direct-answer)))