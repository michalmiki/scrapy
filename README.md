This small project fetch the data from one of the largest polish car advertisment platform and saves output to json. 
Some initial configurations: 

- Autothrottling is enabled 
- Target concurrency is set to 0.5
- Start delay is set to 5
- Max delay is set to 60

Logs are enabled and stored in file "otomoto.log". Due to large logfile produced , log level is set to "INFO" 