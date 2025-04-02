; Main query processor
(= (process-query $question)
   (let* (($kg-response (generate-response $question))
          ($final-response (if (== $kg-response (empty))
                             ((py-atom llm) (user $question))
                             $kg-response)))
     $final-response))