Meeting goals: 

- Introduce background
- Team data analytics focus
- Trust in data
- Risk team composition and skillset
- Technologies used by analyst team (g sheets, notebooks, spark..)
- Data team collaboration principles (peer review, sharing, peer analysis, PRs)

# Data focus
- What is short term? Weeks, months..?
- What is long term? 

# Short term focus: #1 and #3 
  1 get data on liquidity over time 
  2 trades over time 
  3 by-CDP-fees over time
  
  Liquidity over time: 
  - Which liquidity - Vault owner liquidity? 
  - Which platforms liquidity: maker, secondary lending, off-chain exchanges? 
  - Measures of liquidity
  
  Trades by CDP over time: 
  - What do we want to understand? 
  - Are we talking about SCD or MCD or both? 
  - Is categorisation of trades important? (draw, wipe...) 
  - Is categorisation using smart contract ABI decode functions enough? Or maker specific?   
  
 # Longer term focus: 
  - Assessment of new collateral? 
  - Price correlation analysis: Vault behaviour vs Collateral price analysis? Vault holder reaction to collateral price?
  - Modelling: of what? 

 # Data characteristics
 - What data granularity? And time intervals (month, hour, minutes, seconds)? 
 - Preventive analysis? Pending transactions 
 - Off-chain analysis?
 
 # Data trust 
 - What are the sources required? 
 - Does risk team require access to transformation over data? Or only end
 
 
 # Risk team 
 - Who are the consumers of risk data?
 - What is their skillset? 
 - How do they collaborate with each other? 
  + Standards/Frameworks used
  + Platforms & tools
 
 # Tech 
 - Tools and tech used by risk team? Now, future? 
  + Data preparation - how do you read, cleanse data?
  + Data exploration/analysis - notebooks, g sheets etc
  + Data sharing/peer reviewing - co-working
  + Analysis presentation

Other considerations: 
  + Methodology definition & validation
  + Replicability of analysis
  
  # Infrastructure
  - Cloud based - gather/analyse real time
  - Node reliability - pending & confirmation blocks
  - Gather, curation, analysis - on-chain and off-chain data since 2014
 
 # Our team
 - software eng, smart contract devs, data scientists
  - 

  
  
  


  
  
  
  
  
 
