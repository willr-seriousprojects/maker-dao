# MakerDAO

## Contents

- [Risk Governance meeting notes](#risk-governance-meetings)
- [Meeting 2019-05-31](#risk-meeting-2019-05-31)
- [Meeting 2019-06-07](#risk-meeting-2019-06-07)
- [Meeting 2019-06-14](#risk-meeting-2019-06-14)
- [Meeting 2019-06-20](#risk-meeting-2019-06-20)

- [Meeting 2019-08-23](#risk-meeting-2019-08-23)
- [Analytics](#analytics)

<a name="risk-governance-meetings" />

## Risk Governance meeting notes

<b name="risk-meeting-2019-05-31" />

### Meeting notes 2019-05-31

Analysis: 
- relationship between eth and dai changed in dynamic
- supply of dai just been reducing
- age of debt has been reducing -> healthy. costs realised
- what is the right relationship between dai price and price movements? (discussion)
- eth has been taken out of collateralisation -> collateralisation ratio increasing -> impact on secondary lending -> more dai drawn out of Compound and other platforms. Note: DSR supposed to balance out the refinancing dynamic

Multi-collateral:
- collateral analysis required: collateral ratio, liquidity, debt ceiling..
- building out piece-by-piece of analysis
- framework
- SF will be different between assets
- DSR will be same between assets

Next steps:
- understanding of asset and its valuation
- evaluate the risks of asset -> build into risk premium of asset
- how fast CDPs are liquidated

<b name="risk-meeting-2019-06-07" />

### Meeting notes 2019-06-07

Analysis: 
- derivatives and lending becoming an important part of the eth<>DAI dynamic
- refinancing from Mkr to 2nd market platforms has reduced. re: SF reduction
- discussion to have: rate changes between lending platforms
- open debt consistently getting lower than closed debt
- min time scale to see changes from SF reflected in data: **3-5 days**. hard to prevent changes in market conditions within the timescale. re:eth movement is a big indicator. important to keep an eye on 2nd market for inventory.
- collateral ratio: decreasing ratio. re: leverage-seeking behaviour. Usually drop in collateral due to drop in eth value. 
- secondary lending rates: 3-5% buffer between maker and 2nd lending. borrow volumes increasing. 

Risk explanation (Cyrus):
- CDP: exposure risk = insolvency of cdp. Probability of liquidation -> how bad is the exposure. **Needs modelling**. 
  + Action: EAD, LGD, ECL notions need to be modelled and base the SF
  + SF needs to reflect frequency
- risk premium: compensation for risk of liquidation
- bad debt: historically all liquidation has been cleared 100%, with no impact in collateral ratio increase. If that wasn't to happen due to some reason (e.g. reputation risk), we have no
- <> likelyhood of cdp being liquidated 
- collateralisation ratio <> mechanics of liquidation auction
- **important** management of changing risk profiles <> asset-based risk <> different distributions of cdps

New collaterals: 
- framework: how we accept new collateral types. suggestions: 
  + perceived safety of collateral
  + correlation to other assets in portfolio
- 3 steps in evaluation: 
  + classificaiton of collateral 
    + bearer vs non-bearer(bearer asset without counterparty risk e.g. bitcoin. non-bearer e.g. security token)
    + equity/bond tokens
  + due diligence report
    + team/tech/token sale/distribution
  + risk analysis
    + factors leading to adverse market conditions e.g. protocol risk, coding practice
    + valuation models for tokens (frameworks exist)
- community involvement:
  + risk modelling
  + dd analysis
    
**Work to be done**
```
- how to calculate a PUT option on ETH
```

<b name="risk-meeting-2019-06-14" />

### Meeting notes 2019-06-14

Governance (Richard):
- Rational behaviour being applied to voting --> maintenance of the peg, no games played on SF changes
- Question: do we need voting every week? Is delegation of voting possible (e.g. risk team)?

#### Collateral Risk (Cyrus Younessi)

'Collateral Risk Lifecycle' presentation

![](https://github.com/willr-seriousprojects/maker-dao/blob/master/makerDAO%20meetings/Screen%20Shot%202019-06-14%20at%204.30.23%20AM.png)

- Onboarding: 
  + technical audit (smart contracts, connectors, adaptors )
  + risk audit (filter/prioritise assets)
  + counterparty audit 
  + filter and sort
  + governance implications

- This week: Due diligence: 
1. Goal
  + qualitative: find risk not immediately present in the collateral - qualitative understanding
  + scoring: convert qualitative into numeric score 

2. Classification
+ bearer assets 
  - type of token
  - recourse is non-factor
  - downside is high correlation

+ registered assets/STOs/wrapped tokens
  - factor counter party risk in assessment
```
Understanding of tokens to be done
```
Can be either or both bearer/registered: 
- base layer tokens (eth, btc)
- utility tokens 
- work tokens - get paid to do some work
- governance tokens
-  staking tokens 
- security tokens

3. Fundamental analysis (by risk teams)

- Team 
- Technology
- Community
- Business potential
- Token
- Valuation model (ideal) - probably required e.g. `Look into BTC valuation model`

Main risks: What's the worst that can happen with... 
- Money tokens (btc, eth) - Store of value risks
- Utility tokens - velocity risks (in and out of the market). Q: Is branding a factor?
- Work tokens - fork risks
- Governance tokens - value capture risks 
- Staking tokens - technical risks (a lot of risks)
- Security tokens - counterparty risks 

```
All risks will be input into a model --> output probability score
```

4. Risk Analysis
- Adversarial thinking/ Edge cases (How bad can it be?)
  + recourse analysis : what is the risk you don't recover any of investments
  + exchange delistings
  + poor operational management
  
- Event risk not seen in historical trading record
  + Centralised collateral
- Trader's instinct

5. Scoring framework
+ create risk ratings framework and apply to collateral

Examaple - ether

- onboarding collateral application
  + technical audit
- classification
- fundamental analysis
- risk analysis
- scoring framework -> gets transfered to the quantitative model

![](https://github.com/willr-seriousprojects/maker-dao/blob/master/makerDAO%20meetings/Screen%20Shot%202019-06-14%20at%204.58.53%20AM.png)

6. Philosophy 
- conservativism
- common sense
- patience 
- unbiasedness

#### Monetary Policy (Vishesh Choudry)
- increased variability in DAI price 
- trading volume jump. Situation: eth being sold for DAI or DAI being bought to lever up 
- dai supply. has being going down (83M). Short term effect recently with tick up at 16.5%. Also in the secondary lending platforms
- age of debt. debt has being getting younger since 19.5%. Trending has being smoothling. Also in secondary lending. 
- amount of unique users in cdp has increased. 
- colateralisation. rise in mid may. clearing of collateral i.e. deleveraging since eth stabilisation around 240$
- peg. volume trading slightly below 1USD. ```Maybe SF too low?```
- secondary lending behaviour. refinancing has being coming back to maker. re: abrupt spike in rates

#### Narrative (Matthew Rabinowitz)

- VaR vs DSR

<b name="risk-meeting-2019-06-20" />

### Meeting notes 2019-06-20

Governance Segment (Richard Brown)
- Results of the Poll
- Testing the limits of the SF
- Skipping the next SF poll, polling for better polls?

#### Risk Segment (Vishesh Choudry)
Monetary Policy:
- Dai price. Decreased volatility, with slight drift down, despite eth price comming up. 
```
Question: under what conditions does ETH affects DAI?
```
- Dai supply. Slight going up. A few cdps/refinancing back to maker from secondary lending.
- Age of debt. Staddy version.
- Collateral ratio. Previous deleveraging behaviour has been balanced with a slight elevated curve.
- Distribution Dai price. Significant amount of Dai below $1 
- Secondary lending. Borrow-supply has increased long term. But now has been going steddy. Most going to Maker. Re: SF at 16.5% seems to be at an appropriate level. 


#### Collateral Risk (Cyrus Younessi)
'Quantitative Modeling' presentation

Recap from last week
- goal: gather all relavant info and turn into risk rating

[reference to previous week]

Agenda: quantitative analysis outline

[image]

1. Goals
Philosophical
- Dai becomes world currency
- Risk support that mission

Operational goal
- define what risk param represent
- build scientific models for these param
- assess weakness,vulnerabilities of the models
- tie decentralised governance and risk into models

2. Strategy

[image]

- Modular approach
- Academic framework -> Pragmatic
  + start with academic (ideal) framework and work through problems
  + Use of best practices
  
- Start
+ simple model with assumptions
+ conservative liquidity analysis/
+ first analysis with Eth

3. Risk model

Inputs [image]
- Collateral application
- Trading profile
  + Collet trade history
  + Curate wash trading
- Historical cdp distribution

Outputs [image]
- Preliminary outputs
  + Liquidity analysis ("slippage")
  + Collateral risk premium
- Secondary outputs
  + Correlations
- Ultimate
  + 
  
4. Building models

CDPs [example on traditional loans]

Focus: 
- Default risk/ credit risk

Default risk (credit risk)

- start with loss distributions -> mean of distribution
- expected loss 
  + exposure amount (EA)
  + probability of default (PD)
  + Loss given default (LGD)
- applies to all collateral types
 ```
 define default: when cdp is liquidated
 ```

Expected Loss [image]

example
[image]

Goal: quantify expected amount you get back from loan. And how to estimate risk premium from that expected default. 

How to calculate PD and LGD?
- Reputation used in traditional lending 
  + credit scores, employment etc
  + backaward looking 
  + forward looking
- desincentives to default (credit score penalty and **maker cdp**)

Collateral [image]
- two ways loan bust: non payment or collateral values falls 
```
Focus on collateral
```

Types of debt [image]
- Unsecured
- Secured
**- Non-recourse (CDPs)**

Collateral only model
- update PD and LGD definitions
- no scheduled term, payments
- PD = 
- LGD = expected liquidation value of collateral through recourse (**liquidation ratio**)


#### Weekly Narrative (Matthew V Rabinowitz)

<b name="risk-meeting-2019-08-23" />

### Meeting notes 2019-08-23

Governance Segment (Richard Brown)
- Risk team mandate
https://forum.makerdao.com/t/mandate-interim-governance-facilitators/264

LongForWisdom:

#### Risk Segment (Cyrus Younesssi)
Will review and discuss the Risk Teams Mandate
https://forum.makerdao.com/t/mandate-risk-teams/282
https://medium.com/makerdao/makerdao-governance-risk-framework-38625f514101

- Early days: "decentralised risk function" 

How risk teams will operate:

Evaluation of risk models (principles and process)
- Dataset and data being used
  + Verify transparency
  + Filter transformations on data
- Initial risk models with METHODOLOGY used
  + How evaluate token classes
- Applied model
  + Determines the `proposed parameters`for specific token

Next month: 
- General framework: determines the general risk team approach to assess tokens

How to determine risk team: 
- No special priviledges

How does risk team submit risk constructs? (methodology)

Two types of risk teams:
- Sets up model parameters
- Assesses oracles

Risk team compensation
- to be confirmed (voted?)

How incentives are aligned
- Risk teams work in the best interest of MKR holders

TLDR
risk contructs and how models will be presented
risk teams approvals through voting

#### Risk Segment (Vishesh Choudry)
State of the Peg

http://loans.descipher.io/
https://graphs.santiment.net/makerdao


#### Risk Segment (Matthew V Rabinowitz)

<b name="risk-meeting-2019-08-23" />

### Meeting notes 2019-09-13

#### Governance Segment
Richard Brown: Results of Mandate polls (Cyrus and I aren't fired)

Update: 
[Governance at a glance](https://forum.makerdao.com/t/governance-at-a-glance/84)
[Signaling process](https://forum.makerdao.com/t/current-signaling-process/396)

LongForWisdom: Governance at a Glance
- USDC request for onboarding
- Cadence of votes: one week or longer

#### Oracle Segment (Nik Kunkel)
- Head of Backend Services will continue his tour of the new Oracle systems

- Last week: oracle ecosystem within maker
+ number of proposals will be posted
- Mariano Conti
+ Original architect of oracle ecosystem

- Why are doing this?
+ gradual decentralisation of the community

[image] - oracles and defi feeds
[Image](https://lh5.googleusercontent.com/hEvf8MBZCEJ-jQB_j8Rdgb9k3H36fT7iJttX2oVsyQgTXb1LDV7G50NxvWan98HOU4KFvAEKpR0H5k8dV6Uvz0WaJogZzWMVZqySxx8Z2wAFJb33KmndFd1G9pPtGurI1Gmv9b_E)

Oracle

Feeds (def):
+ humans or organisations running bots that source price for assets and signs 
+ inputs for oracle smart contracts (ie. canonical prices for sc)

Whitelisted add: 
+ smart contracts that can read asset price data from feeds, against payment.
+ whitelist doesnt need to be used right away
+ whitelist add doesnt need to be paid for (necessarily)
e.g. DEX using DAI as primary asset

#### Risk Segment (Cyrus Younesssi)

**Will review and discuss the Risk Teams Mandate**

**DSR**
Where the DSR comes from? How it is created?
+ DSR contract just functionality to create new DAI, without any collateral
+ DAI created is weighted against SF. If too much DAI create, then flagged as "bad debt"

What to do with this extra cost for MKR?
+ Price up in collateral if simply pass to CDP holder
+ Would it make sense to add SF if collateral type was too popular?

Proposal: 
+ Change SF once a month
+ Change DSR more often

Expectation: 
+ increase in DAI supply over near future

Questions: 
+ Any thoughts around a pooled model for DAI locked in DSR with an underlying token that has a claim to the asset pool? (Similar to Compound) 
+ After DSR, when making changes to DSR/SF, will both be moved at the same time, or will the DSR be preferred over the SF? 
+ At what rate should the global debt ceiling be increased?

Update:
[Update on DSR](https://forum.makerdao.com/t/an-update-on-dsr-and-initial-values/433)

#### State of the Peg (Vishesh Choudry)
Vishesh Choudry: State of the Peg

+ ETH stable over last week
+ Reflection in collateral locked. About same.
+ A few drops in SF
+ Debt. Amount of debt being increasing 
+ As ETH price drops, increase in collateral. 
+ DAI peg. Sligth over 1usd. Lower volume affects VWAP bell curve (normal distribution)
+ Secondary lending. Lending rates decreasing. dydx increased in borrow volume. compound reduced. Together: 30M
++ Decreasing SF increases borrow volume on secondary lending
++ Excess outstanding supply increasing in 2md lending. Concerning considering reducing i SF?


<b name="risk-meeting-2019-10-11" />

### Meeting notes 2019-10-11

#### Governance Segment

Rune: Where is maker and DeFI today? (talk at DevCon)

[image]

- composability
+ how to scale DAI to billions in supply?

- tokenised real assets into blockchain > supply side
+ upgrade legacy system

- reconcile regulation and decentralisation
+ important to all crypto
+ regulate on the edges e.g. Security tokens, Exchanges
+ diversify jurisdiction to prevent full maker crack down
+ examples: USDC, Compound

- synthetic assets (?) > demand side scale
+ emulate any asset with low overhead e.g. euro 
+ no difference for MCD deploy in maker
+ consolidate liquidity
+ example: create synthetic gold related to real gold traded in markets




















