# MakerDAO

## Contents

- [Risk Governance meeting notes](#risk-governance-meetings)
- [Meeting 2019-05-31](#risk-meeting-2019-05-31)
- [Meeting 2019-06-07](#risk-meeting-2019-06-07)
- [Meeting 2019-06-14](#risk-meeting-2019-06-14)
- [Meeting 2019-06-20](#risk-meeting-2019-06-20)
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


























