if(!require(rworker)){
    install.packages("rworker")
    library(rworker)
}
if(!require(magrittr)){
    install.packages("magrittr")
    library(magrittr)
}

url <- 'redis://redis_r:6379'
rwork <- rworker(name='celery', queue=url, backend=url, workers=2)

(function(){
  # Simulating long running function
  Sys.sleep(10)
}) %>% rwork$task(name='long_running_task')

(function(){
  # Another dummy function
  print('Hello world')
}) %>% rwork$task(name='hello_world')

(function(){
  Sys.sleep(5)
  task_progress(50) # 50% progress
  Sys.sleep(5)
  task_progress(100) # 100% progress
}) %>% rwork$task(name='task_with_progress')

rwork$consume()