# MakerDAO

## Contents

- [Risk articles on Defi](#articles)
- [Data sources](#data)
- [Risk Governance meeting notes](#risk-governance-meetings)
- [Meeting 2019-05-31](#risk-meeting-2019-05-31)
- [Meeting 2019-06-07](#risk-meeting-2019-06-07)
- [Meeting 2019-06-14](#risk-meeting-2019-06-14)
- [Meeting 2019-06-20](#risk-meeting-2019-06-20)
- [Meeting 2019-08-23](#risk-meeting-2019-08-23)
- [Meeting 2019-10-11](#risk-meeting-2019-10-11)
- [Meeting 2019-10-18](#risk-meeting-2019-10-18)

- [Meeting 2019-12-06](#risk-meeting-2019-12-06)
- [Meeting 2019-12-13](#risk-meeting-2019-12-13)
- [Meeting 2019-12-20](#risk-meeting-2019-12-20)
- [Meeting 2020-01-03](#risk-meeting-2020-01-03)
- [Meeting 2020-01-10](#risk-meeting-2020-01-10)
- [Meeting 2020-02-10](#risk-meeting-2020-02-14)
- [Meeting 2020-02-21](#risk-meeting-2020-02-21)
- [Meeting 2020-02-28](#risk-meeting-2020-02-28)
- [Meeting 2020-03-13](#risk-meeting-2020-03-13)

- [Analytics](#analytics)


<a name="articles" />

## Risk Articles

Collection of relevant analytical articles to understand risk categories, metrics and analysis associated with Maker and DeFi platforms. Focus on factual data and scientific research

- [Illiquidity and bank runs in DeFi](https://medium.com/alethio/overlooked-risk-illiquidity-and-bank-runs-on-compound-finance-5d6fc3922d0d#3f8c) by [Alethio](https://medium.com/alethio)

<a name="data" />

## Data sources

- [Blocklytics Ethdata](https://blocklytics.org/) by Blocklytics - tool to help Python analysts and developers focus on analysis instead of pulling and decoding Ethereum data. 
  + [Documentation](https://docs.blocklytics.org/ethdata/introduction)
  + [Blog](https://blocklytics.org/blog/ethdata-python-module/)
  + [Pools](https://pools.fyi/#/) - liquidity pool tracker by Blocklytics
  
- [Dune Analytics]
  


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


#### State of the Peg (Vishesh Choudry)
Vishesh Choudry: State of the Peg

+ DAI: healthy state of the peg.
+ Secondary lending: compound borrow rate more expensive than maker. 
+ Outstanding supply: little change.
+ Excess supply: little increase
+ Utilization rate: compound reduncing relatively. 
+ Tx volume


<b name="risk-meeting-2019-10-18" />

### Meeting notes 2019-10-18

#### Governance Segment
Richard Brown: Ecosystem and Governance implications of Multi-Collateral Dai launch

MCD:
- engagement with the real world
- increase of liquidity in the system
- build a portfolio of assets
- stronger security modules. mitigation of risks
- SCD and MCD work in parallel

DSR: 
- subsidy of activities

Questions: 
- How do we maintain stability of MCD and SCD?
- How long will we maintain MCD and SCD in parallel?
- How will we manage the upgrades of MCD with a bigger ecosystem? How will we de-risk this process?

LongForWisdom: Governance at a Glance

### Risk Segment

#### The migration process and its implications for Risk.
Cyrus Younesssi

What will happen with SCD? 
What will happen with Global Settlement?

MKR holders are safe guards of the user base
Risk's job: 
- assess the options and suggest pathways 

Migration. How it works?
- two types holders: mkr and dai (sai)
- migrate mkr and sai holders. operarational concern more than risk. 
- migrate 85M sai into 85M dai. Risks in chaotic scenario:
  + supply chocks
  + pump-dump in sai and dai

- Solution: migration contract
https://github.com/makerdao/developerguides/blob/master/mcd/upgrading-to-multi-collateral-dai/upgrading-to-multi-collateral-dai.md
  + cdp owners: can atomically migrate with the above. 
  + requires MKR migrated first
  + requires sai in the deposit contract

**How the migration governance will work?**
- From January: more proper risk models
  + risk model param at launch are conservative rather than accurate.

#### State of the Peg
Vishesh Choudry 

Pricing: stable. avg 1.05usd. Majority above 1usd
Volume: 13M 7 days
DAI supply: run up amount in supply mid-sept
Collateral: slight increase in amount in the system
ETH prices: quite over last week
ETH collateral: locked is growing. Wipe: lower level of increase
ETH price and Liquidation: few liquidations recently
DEBT: responsiveness of supply to eth price
Secondary markets: borrow volumes are flat. supply volume slight increase. 

<b name="risk-meeting-2019-12-06" />

### Meeting notes 2019-12-06

### Governance Segment
Richard Brown: Governance Challenges

LongForWisdom: Governance at a Glance
- DSR vs SF spreads

### Risk Segment
Cyrus Younesssi: Migration Status

[image]

- Total debt ceiling vs current debt ceiling
- DSR utilisation rate dropped. All exchanges have not dropped users DAI into DSR
- SAI supply has fallen re: exchange migration
- SAI vs DAI supply about 50/50
- SAI below 1usd for some months --> risk still upside if "panic"

Liquidity strategy
[image]


questions: 
- "hoarding attack"?

daistats.com
sai2dai.xyz
instadapp/defisaver


### Risk Segment
Vishesh Choudry: State of the Peg

General Q&A


<b name="risk-meeting-2019-12-13" />

### Meeting notes 2019-12-13

#### Governance Segment
Richard Brown: Governance Challenges

LongForWisdom: Governance at a Glance
- Emergency shutdown read - interesting
- Vote for DSR as f(x) of SF
- Emergency change to SCD [post](https://forum.makerdao.com/t/signal-request-poll-when-should-we-trigger-scd-global-shutdown/935)
- Poll to activate governance security [post](https://forum.makerdao.com/t/addendum-to-the-current-poll-to-activate-the-governance-security-module/938)
- Governance security module vs monetary policy vote [post](https://forum.makerdao.com/t/in-the-case-where-an-emergency-technical-change-to-the-dcs-is-required-should-we-skip-monetary-policy-changes-in-that-weeks-executive-vote/929)

#### Technical Segment
Wouter Kampmann The Governance and Oracle Security Modules<>br
[original post](https://forum.makerdao.com/t/addendum-to-the-current-poll-to-activate-the-governance-security-module/938)
- delay: allows to inspect effects in the system -> community can remediate OR emergency shutdown mechanism
- vote also required for patching fix
- oracle security module does not need vote -> 1h to application

#### Risk Segment
Cyrus Younesssi: Migration Status<br>
- Migration: DAI more than SAI
- DSR: 4%
- DSR utilisation does not push dai price up. Move from usd to dai does. 
- Higher dsr = less float
- DAI in uniswap liquidity higher than SAI
- CDP holders are still bottleneck in migration. Not dai holders.
  + strategies to push migration
- Compound has significant SAI holders

Vishesh Choudry: State of the Peg<br>
- Trading around 1usd. Light trading.
- 96% of DAI from eth. 3% from BAT. 
``
More thought needed on more collateral added. Conversations on-going
``
- Borrow rate
- Compound: supply still pretty high

<b name="risk-meeting-2019-12-20" />

### Meeting notes 2019-12-20

#### Governance Segment
Richard Brown: General Q&A
+ Shareholders are mostly following community position

LongForWisdom: Governance at a Glance
+ Pooling
+ [Signaling requests guidelines](https://forum.makerdao.com/t/signaling-guidelines/223)
+ https://community-development.makerdao.com/makerdao-mcd-faqs/faqs/emergency-shutdown
+ https://forum.makerdao.com/t/questions-discussion-on-the-emergency-shutdown/930
+ Debt per collateral bucket: 225%-325% mostly. 
```
Opportunity: run time series view of bucket collateralisation by eth price 
```

#### Risk Segment
Cyrus Younesssi: Migration Status
+ Compound migration coming soon
+ Debt ceiling: DAI Debt ceiling near the limit

Vishesh Choudry: State of the Peg
+ DAI Price: around 1usd. V
+ SAI trading olume is picking activity : dydx, khyber, oasis 
+ Surplus of DAI going into DSR

<b name="risk-meeting-2020-01-03" />

### Meeting notes 2020-01-03

#### Governance Segment
- presentation of governance model
[images]
+ [presentation](https://docs.google.com/presentation/d/10x5Z0111Lt6tOMsqhiZop53QiLLSRxqaQKVvyPY6D-U/edit)
+ [Original thread](https://forum.makerdao.com/t/signal-request-should-we-replace-the-weekly-dsr-rate-governance-poll-with-a-dsr-spread-governance-poll/969)

#### Risk Segment
Cyrus Younesssi: Migration Status
+ ETH debt ceiling 100M
+ MKR in burner - 10K
+ Worry: Compound SAI
+ Santiment: 6M SAI not moved in 1y+ --> [analysis here](https://graphs.santiment.net/makerdao-pro#event_stats)
+ Distribution: 100 addresses hold 1/3 of SAI

Vishesh Choudry: State of the Peg
+ Secondary lending SAI: not moving much
+ Parameters to consider: dsr, sf, avg borrow rates, avg lend rates
+ collateralisation ratio: measure of risk in the system - low collateral about 1/2 of DAI supply!
  + 3 CDP account for 23 out 73 MCD
+ maker burn [here](https://makerburn.com/)

<b name="risk-meeting-2020-01-10" />

### Meeting notes 2020-01-10

#### Governance Segment
Richard Brown: General Q&A
Derek - emergency shutdown module

#### Risk Segment
Cyrus Younesssi: Migration Status (done by Primoz)
- DAI supply pickup: new CDPs open in SAI (market makers or speculators?)
- SAI liquidity. Uniswap is only way. Slipage is increasing.
- Improved coll ratio
- DAI in DSR: increased due to addition of compound
- SAI CDPs: 7M SAI in inactive wallets; 7M in known addresses; top 100 addresses own 77% of SAI
  + Migration is limited by liquidity -> not enough SAI to pay debt on CDPs
  + Recent addition of ETH to prevent liquidation
- SF fees paid in MKR increased

Analysis at
https://docs.google.com/spreadsheets/d/1Ba972aexu2-KQ0hyGxs8XbZZG05N-WTkmMJf6DutZxY/edit#gid=1147677054

Vishesh Choudry: State of the Peg
- DAI VWAP breakdown 
- SAI: low volumes, mostly in uniswap
- Collateration ratio: low collateral for significant %

```
Opportunity: how much of CDP activity is managed automatically
```
<b name="risk-meeting-2020-01-17" />

### Meeting notes 2020-01-17

#### Governance Segment
Richard Brown: General Q&A

LongForWisdom: ‘Governance at a Glance’

Mariano Conti: Maker Burn

#### Risk Segment
**Cyrus Younesssi: Debt Ceilings**
- SCD: 70M ceiling. Big gap of unused debt ceiling > option: reduce Debt ceiling
- MDC: increase in eth collateral. Will hit debt ceiling soon.  
  + Short term debt celing > no pre-eventive action to increase yet
  + Long term theoretical max DC

**Primoz Kordez: Migration Status**
- DAI supply: 89M > 12M increase since Jan 1
- SAI-DAI migration increasing (through contract)
- New draws: 20 CDPs (draws) > increasing debt (25% of debt)
- Net wipes: 27 > reducing debt 
- Inacticve CDPs during migration: 32 > 12M in debt (41% of debt)

Analysis at
https://docs.google.com/spreadsheets/d/18Et6TQZnGfuc8YJXHLFZXm75UzxigGR3wcp8VaibhdI/edit#gid=1942156439

```
analysis opportunity: what are CDPs minting SAI doing with debt? 
```

**Vishesh Choudry: State of the Pegs**
- Vaults MCD: top 20 vaults hold 44M of outstanding DAI supply

```
Opportunity: historical vault analysis required
```


**Derek Flossman : Current thinking about Tax**

- Shutdown of SAI CDPs > when global settlement occurs debt is forgiven
  + optional solution: tax penalty to CDPs
  + 6 months repayment phase followed by tax date
  
[images]

<b name="risk-meeting-2020-01-31" />

### Meeting notes 2020-01-31

### Governance Segment
Richard Brown: General Q&A

LongForWisdom: Governance at a Glance

#### Risk Segment
Vishesh Choudry: State of the Peg


<b name="risk-meeting-2020-02-" />

### Meeting notes 2020-01-31

### Governance Segment
Richard Brown: General Q&A

LongForWisdom: Governance at a Glance and 'A Very Special Thread'

[Governance dashboards](mkgov.science)
```
analysis opportunity: what kind of historical data required for governance
- increase in vote participation
- how much MKR is activate in a day (avg)
- time since last active address = measure activity 
```

### Risk Segment

```
analysis: SAI risk 
```

**Primoz Kordez: Migration Status**
- DAI supply: largest migration came from nexo. 2 large cdps migrated . 
- Coll ratio: has increased significantly (400+). Reason? Bullish?  
- no SAI minting activity recently. makerscan 
- SAI liquidity: still some liquidity in Compound
- 

[defiexplore](defiexplore.com/stats) - only aggregated view of dai migration
[makerscan](makerscan.io/cups) - minting activity for SAI

```
analysis opportunity: why is coll ratio increasing? Bullish sentiment? CDP migrations?
```

[stopped at 55min of meeting - re-watch from here]

Vishesh Choudry: State of the Peg

<b name="risk-meeting-2020-02-14" />

### Meeting notes 2020-02-14

### Governance Segment
LongForWisdom: Governance at a Glance
- Update to the state of the peg dashboard/section
- signal request for new `ETH debt ceilling`: should maker or risk team to make decisions?
- cyrus: debt ceiling happens in incremental way due to OSM
- DAI auctions: mostly 1 person bidding [makerburnauctions](https://daiauctions.com/) and [surplus auctions](https://daiauctions.com/flap)
  + Suggestion: reduce spread in auction (min bid 3%) to encourage competition  
  + Flash loans: won't work probably..

WillBarnes: conflicting Governance attack for GSM
- Proposed solution: Dark Fix
  + Bug fix is kept secret (bytecode) --> `create_to_opcode`
  + GSM delay can be introduced
  + Cryptographically secure
  + emergency shutdown can be triggered, despite dark fix
- Trust building with community
  + MKR stakeholders sign message to signal support 
- Summary
  + good balance between governance attacks vs critical vulnerability
  
- Code at [here](https://github.com/makerdao/dss-darkfix)
  
[stopped at 48min of meeting - re-watch from here]

### Engineering Section
Mariano Conti: "Dark Fixes and the GSM"

### Risk Segment
Primoz Kordez: Migration Status

Vishesh Choudry: State of the Peg

<b name="risk-meeting-2020-02-21" />

### Meeting notes 2020-02-21

### Governance Segment
Richard Brown: Governance Security Module: A Brief History

Current GSM Thread

- Dark Fix Thread
  + In the future: easier to shutdown and bring back up system. ie 2 transactions

- Previous Failed GSM Vote
  + Another vote will take place in 24h. Increase gsm to 24h
  + Technical emergency takes precendent over monetary policy
  + SCD is an attack vector to MCD ("back door"). Should GSM protect SCD?
  
GSM Technical Docs

LongForWisdom: Governance at a Glance

### Technical Segment
Engineering will discuss the specifics of the Governance Security Module and the 'Dark Fix'

### Risk Segment
Primoz Kordez: Migration Status

**Vishesh Choudry: State of the Peg**
+ DAI volume: Higher trading volume than normal. Mostly on Dydx. 
- Coll ratio: meaninful risk. Distribution with >30% in low coll ratio
  + There was reduced eth from contracts > due to flash loan attacks?
- Debt amount: increased up until a dip
- MKR liquidity: 
  + 16k > 4K liquidity in uniswap in last week -> defending system? (2 main whales)
  + a script underway for mkr liquidity from different platforms

[stopped at 48min of meeting - re-watch from here]

<b name="risk-meeting-2020-02-28" />

### Meeting notes 2020-02-28

### Governance Segment
- cadence poll: reduce dsr spread candence 
  - [Pool vote](https://vote.makerdao.com/polling-proposal/qmxvvzb6uei1jawvtxentsbreepfkuzsohaefpw6j4vpn5)
  - [science gov](https://mkrgov.science/poll/104)
  - [thread](https://forum.makerdao.com/t/signal-request-reduce-the-frequency-of-the-dsr-spread-governance-poll/1207)
- single thread: rank choice option

Book to read: "Thinking in Systems: A Primer" by Donella Meadows.

### Oracles Segment
Nik Kunkel: Oracles and Governance
- New oracles are being built
- Oracles: are data suppliers > used for collateralisation, price
- MKR oracles are backbone of DeFi > used by many dapps
- Feeds: set of individuals/org that submit data to oracles > appointed by MKR governance
  - Dark feeds: Identities of feeds unknown > no sybil resistance; users don't trust 
  - Light feeds: Orgs with public identities 
    > well known with communities and brands 
    > have a reputation to protect
    > ideal: hybrid between Dark and Light feeds
- Oracles v1: feeds > contracts > medianizer (median) > dsr contracts
- Oracles v2: use eth to sign feeds offchain , use gossip network > most happens **off chain**
  - feeds > scuttlebutt p2p gossip network > relayers > medianizer > oracle security module > Dai stability system / Customers & partners
  - increases scalability, reduces attack
  - Customers & partners can choose if use oracle security module or read from medianizer

- Governance: how does it play here?
- Administrative power: add/remove feeds, add/remove oracles, change delay period in OSM, manage whitelist read-access to oracles
- Current state: 
  - migration from v1 to v2 at least until SCD is out
  - any oracle for free for 1 year
- Oracle team mandate
  - Risk team has mandate as SMEs

Next steps:
- Process to get whitelisted? 
- How to become a light feed?
- **By next week document on processes (DRAFT)**

```
ChainLink: has problem with updates with congestion of on-chain network
```
```
Oracle v1: Maker does not know who/how they use the oracles. V2 Maker will know who/what and whitelist
```

### Risk Segment
Primoz Kordez: Migration Status
- SAI migration in migration contract (avg: 300K/day)
- active SAI cdps have been deleveraging
- share of inactive wallets is rising 

Vishesh Choudry: State of the Peg
- Dai trading slightly above peg (24h)
- DyDx and Oasis activity high > dydx short term positions, higher yield
- Deleveraging happening en masse > More eth--> DAI
- Top 3 positions > 25% of supply!
- Liquidity increasing in Uniswap but not to market speed
- Auctions increased in last 24h

<b name="risk-meeting-2020-03-13" />

### Meeting notes 2020-03-13

### Governance Segment
Richard Brown: General Q&A

Suggestions from discussion:
- lower dsr spread
- delay debt auction time 
- keeper liquidity for auctions

Links: 
https://forum.makerdao.com/t/black-thursday-response-thread/1433
https://github.com/makerdao/developerguides/blob/master/keepers/auction-keeper-bot-setup-guide.md
https://mkrgov.science/poll/110


https://forum.piedao.org/t/community-call-1-kick-off-defiscore-cash/59

```
Opportunity: Any financial models been created looking at Keeper costs vs potential profits to see what kind of spread is required to be profitable/attractive to setup?
```

```
Opportunity: analyse auction bids
```

### Risk Segment
Cyrus Younessi: Collateral Risk Part 2

Vishesh Choudry: State of the Peg


<b name="risk-meeting-2020-03-18" />

### Meeting notes 2020-03-18

### Governance Segment
Richard Brown: General Q&A

### Risk Segment

**Vamsi’s presentation on the Flop Auction**
- PRESENTATON

**Dockerized auction keeper presentation by Marc-andre**
- Very interesting presentation

```
Opportunity: start out with docker version of keeper software (github)
```

Flop Auction: Potential executive vote to lower minimum bid. Pros/cons?
- start price for debt auction
  - do we want to decrease start price of bidding amount (current: 200)? e.g. 166 DAI per MKR
  - speculation: shall we reduce to "free market" approach ie 0 bid starting price
  > risk: inflation 
- original: flop auction 48h after liquidation > increasing to 6 days
- failed auction = auction without bids

```
opportunity: liquidity analysis 
```

**USDC overview / recap +
Circuit breaker discussion. When/how to use.**

- circuit breaker = liquidation freeze
- circuit breaker allows for time to reduce crunch from auctions

- issues: network congestion and dai liquidity
> node infrastructure --> related to the 6h TTL
> dai liquidity issue not solved --> ISSUE

Look at projected required DAI
http://makervaults.descipher.io/

- add USDC helps with DAI peg and dai liquidity crunch > DATA to prove
> reduces the issue with liquidity required for a big drop in ETH

Rational behind USDC:
```
So if the DAI price skyrockets in the event of an eth drop ppl can basically 
get DAI backed by USDC so that keepers have availability of DAI to close auction lots.
```

**SCD shutdown discussion. Data collection.**
- explore.duneanalytics.io/dashboard/cdp-migration

Reasons for cdp migration (speculation)
- peth dilution if it comes to losses
- capitulation, migrate and close cdp

Reasons to migrate sai
- premium available when migrating to DAI at 13% higher price
- high dai lending rates

If eth drops, there is sai liquidity crunch > mostly below 70 USD

Summary: 
- if eth keeps dropping, sai liquidity get short for auctions.
- if eth keeps dropping, incentive to migrate to DAI (premium)

