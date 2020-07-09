# Team profile

## William
- Tech startup & blockchain experience (professional services)
- Founder of analytics company focused on blockchain/crypto analytics projects
- Traditional banking experience = Credit Risk Management (Retail mostly) & Data governance (Risk and enterprise)

+ Risk analytics:
    + design of stats champion-challenger strategies/policies
    + credit origination & collections/recoveries experience
    + system implementation of strategies w/ analytics & Big Data tools (Experian & Cloudera)
    + risk portfolio analysis & recommendations = stats on policy strategy implementations
    + risk modelling = origination app scores & collection behavioural scores
    + portfolio => Consumer finance (Mortgage Lending, PL, CC, OD) & SME. Some corporate lending experience

+ Blockchain: 
    + professional services delivery w/ software engineering teams 
    + serverless product development (ChainOps). Cross chain tx, add factory, payments integration (Stripe)
    + wallet design & integration
    + technical documentation
    + test driven development
    + smart contract security auditing 
    + Solidity/Javascript code review
    + Blockchain analytics data pipeline architecture/design
    + clients: BNC, Zippie, MobileGo, MyBit, Shapeshift, tZero, SharesPost, HyperLink

- Skills:
    + Software engineering
    + Agile data science
    + SQL
    + Python (analysis & predictive modelling)
    + Data science distro & frameworks (Anaconda, Numpy, Scipy, Sklearn..)
    + Javascript & Solidity (Reading proficiency)
    + Cloud: AWS (S3, DynamoDB,SageMaker) & GCP (BigQuery, DataStudio, Data Lab)
    + Getting started AWS DevOps & Linux/Shell scripting

## Hock
- Risk analytics professional (consultant)
- Senior modeller & Analytics Manager in Risk Management and Ops & Compliance
- Forex trader & e-commerce startup founder

- Risk analytics specialties:
    + Probability of Default models (predictive) using BASEL II & III capital requirements
    + Knowledge/experience BASEL II & III frameworks
    + Retail risk PD models
    + Ops Risk & Compliance Retail & Wealth Management = Management
    + Private & Wealth risk management
    + PD model development for 3 banks in NZ

- Other experiences:
    + Market reseach analytics
    + Supervised & Unsupervised ML techniques = predictive models for clients (NZ & overseas)

- Skills/interests:
    + Masters of Science
    + SAS, R analytics
    + Getting started in Python
    + Forex trading
    + e-commerce

# What we can do (skills/delivery)

Dashboard:
-  Monetary policy tracker

Modeling:
- Risk framework Monte Carlo simulations
- Complex systems-based modelling/simulations
    + e.g. CompoundFinance 

Deeper analytics: 
- network analysis graphs of DAI transactions & network liquidity: onchain, offchain
- network analysis graphs of MKR transactions & tokenholder decision making (events, liquidity, policy decision making) 
    - e.g. contribution to governance analysis of incentives


Adhoc analysis: 
- MCD
    - Time series analysis on outstanding DAI distribution by vault holders
    > e.g. top 20 vaults hold X amount of DAI
    - Collateral ration dynamics

- SCD
    - CDP activity management by holders = automated vs manual
    - Debt use by CDP holders. What is the minting used for?

- Governance analytics
    - increase in vote participation
    - how much MKR is activate in a day (avg)
    - time since last active address = measure activity

# What else maker needs

---

Meeting with Rich/Cyrus

# Proposal (From Rich)

grants proposal 
- immediacy and analytics 

Risk proposal:
- 1 to 2 page exercise
- Include high level summary and technical description
- proposal description:
    - what work will be done
    - how it will be delivered (format)
- How many phases of model delivery
- How long to deliver each phase
- What is the budget required

Things to consider
- dependencies
    - data
    - technology
    - risk teams

- Costs
    - tech infrastructure (AWS, GCP)
    - hourly work/project budget

---

Meeting with Cyrus/Hock

# Proposal presentation meeting 2020-05-01

Rough agenda (from Cyrus)
```
# go over the proposal. there's a lot in there, a lot to discuss. 
# i'm thinking of focusing/narrowing the scope a bit too. 
# also, i want to talk about some medium term stuff, like some of the new collateral applications that have been coming in
```

1. Proposal presentation
2. Focus of proposal
3. Collateral application analysis(?)

## Actions
- review proposal 
- note down potential questions or scenario building
- review top collateral for onboarding


## Proposal

Two parts:
- Auditing of risk model and framework
- Probability of liquidation model

**Auditing**

Why?
- independent oversight to validate: methodology, data, theory, testing
- Maker gains stakeholder trust in the model/framework choices
- Validation provides greater authority when using framework for recommending decisions for governance
- Evaluate use of model against original intent (i.e. methodology, assumptions at inception)
- Best practice approach

How: 
*Two stage approach*
Assessment of risk and modelling framework
Validation testiing 

Why this approach
- Proven best practices in traditional financing settings

What? (delivery)
- document detailing appraisals on Risk framework and modelling 
- Validation testing results detailed

Other spillovers:
- Understanding model assumptions and choices made (in theoretical choices, methodology and data)
- Assess possible use of parameters (specially systemic ones) in Probability of Liquidation Model

**Probability of Liquidation Model**

Why?
- isolate idysuncratic risk systemic risk
- assess risk factors that contribute to losses
- quantify risks inherent to maker > view of **idisyncratic risks**
- quantify/assess underlying market forces that impact maker losses > systemic risks

- quantify the relationship between parameters and risks 
e.g. collateral ratio <> losses relationship > quantify through modelling

How: 
- systemic risk & idiosyncratic

*Two stage modelling process*
> Idiosyncratic model in relation to losses
```
actual losses - predictive losses from idiosyncratic param = residuals or error terms
```
> residuals assumed to be explained by systemic risks
e.g. market forces (user bahaviour, macro economic factors like gdp, liquidity etc)

Added value: 
- establish two sets of risk (idiosyncratic & systemic)
- simple model to establish relationship btw outcome & idiosyncratic (inherent to maker to influence outcome)
- add-on with systemic risk

What? (delivery)
- frequent/weekly progression of analysis
- transparency of methodology choices, data used (inputs, analysis, wrangling) and model (building,testing)

Spillovers from model:
- assert analysis from governance
- how risk parameters influence the outcome (loss)
> how each of the parameter influence profit/losses

## Collateral application analysis

A few proposed: 
- Binance Coin
- REP/Augur
- DGX (gold IOU)
- WBTC
- SNT (Synthetix)
- Stablecoins: tUSD, EURS, Tether
- Uniswap Liquidity
- FTM

Short term focus/needs
> Collateral evaluations 
- WBTC
- DeFi stablecoins
- Link and other crypto assets
- Centrifuge -> next -> take a stab at real world assets

Tricky/Pain
- give grant for auditing model > luxury
- no understanding of the 2 phases of proposal
- real practical work required for collateral evaluation
- no view of practical risk experience
- justify theoretical work vs 

Releave pain
- Practical work with collateral evaluations
- Be the second risk team
- Take/be able to take up
- Package deal: collateral + risk modelling (please)
- Easy pitch to Maker with onboarding new collateral > centrifuge collateral
- Commit to certain nb of hours by month > monthly bill 
- Be on track for collateral vs 
- Things change and we need adaptation > not too specific about which collateral

In parallel
- build theoretical model framework

Improvements
- dashboard provision specifically for modelling
> maybe merge with Maker suite of dashboards

Phases 
- collateral risk
- monetary policy

Collateral risk
- tokenising real assets is hard (legal)
- real business asking for loans
- traditional loan instruments as leverage facilities 
- very diverse applications
- use centrifuge tokeniser
    + paperchain - tokenise spotify royalties
- maker will be a leverage facility for these companies. Other than ETH. 
> ie collateral against DAI

What kind of work
- assess in terms of risk  > risk grading of companies 
- translate risk rating into numerical risk parameters within ecosystem 
> ex: risk loans for small business 
- debt ceiling, liquidation ratio and SF > LTV, interest rate and notional amount of loan > LGD (liquidatio ration), Risk premium (SF), exposure (debt ceiling) 
- freedom to handle

What components are needed:
- exposure: combined debt
- industry benchmark: 
- PD, EAD, LGD


Examples
- [Paperchain](https://forum.makerdao.com/t/pc-drop-mip6-application-paperchain-drop-tokenized-music-streaming-invoices/2215)
- [Consolfreight](https://forum.makerdao.com/t/cf-drop-mip6-application-consolfreight-drop-tokenized-freight-shipping-invoices/2214)

Company types
- traditional loan instruments for SMEs
- "shitcoins" projects with tokens 

Governance
- show the work done
- risk parameters
- no shortage of work at MakerDAO

Expectations for collateral onboarding:
- a lot of applications in coming months
- 2-3 per month (rough estimate)

Easy ones
- paxUSD
- tUSD

Harder ones
- Link/TBTC

Next steps
- slightly alter proposal to include collateral evaluations
- compensation budget/ monthly quote
- prior risk work
- general framework about how to go about collateral evaluations
> what the approach to be pitched to the community

MIPS
- Auditing the methodology via the community MIP

--- 

# Update 2020-05-15 (Cyrus)

- Goal: Update on proposal
- Make sure comfortable with direction we're taking

- Recap problem: Acknowlegde key problem we're solving: risk assessment to collateral onboarding (mostly for traditional business backing loans with traditional collateral)

- Two step to address problem in proposal: 
1. Provide a grading mechanism with both financial/non-financial analysis. To assess risk quality of business and CAPACITY to service the debt
2. Map risk assessment (grading) to risk parameters

# If asked only:
- Advantages of grading/reasons for grading:
consistency of evaluation across companies and sectors
using best practices in sme risk frameworks (practioner/academic review)

# Key points:
- we're are on track to send proposal: starting 25 may week
- I want to make sure you're comfortable with the approach we're taking
- I want to make sure that when you get the proposal it will be of value to Maker

- We need to refine second step of the process, with the calculations we intend to put in place

Announcing future: 
- it has taken more work than expected
- there are greater challenges with estimating 
#1 quality of applicants, health of the business and CAPACITY to service debt and
#2 risk of default and expected losses to assess the right "pricing of the deal" (or loan structure). 
- little statistical data that allows putting companies into distributions (PD, StdDev, Clustering)
- simulations will likely be the path to help bridge the gap

- Because of this, we need more work to lay the foundations

----

# Update 2020-05-29 (Cyrus)

Three possible scenarios on updated proposal, from worse to best
1. No, thank you (worse)
2. Yes, but... (good, most likely)
3. Yes, when can you start? (best)

# Strategic approaches to each

## 1. No, thank you (worse)

Desc: we've given two chances and proposal is not fit for requirements

Outcomes: 
- Try to obtain reasons for dismissal 
- Try to clarify possible paths out of dismissal 
- Propose alternatives or workarounds to address concerns (reasons announced)

Howto: "how" and "what" questions
- How does this proposal not meet your requirements? 
- What is your concern about our methodology?

Ennunciating setences: 
- Grasp from sentences announced and re-phrase as "how..."?

## 2. Yes, but... (most likely)

Possible "buts" 
- Price 
- Methodology
- Proposal review (again)

**Price argument**: "You're too expense" / "Not enough value for money" 

Mise en scene: Repeat
- we have invested time to put a good proposal together (free of charge)
- we're not only generalists but also bring industry experience (Credit Risk)
- how are we supposed to accept that (proposed) rate?

Calibrated questions:
**- How is it not enough value for money?**
**- How is this too expensive? "We pay our own analysts less"**
**- Other than money, are there other sticking points?**

Arguments: 
- extensive banking experience 
- provide value of both generalist and experienced members in risk team
- this is reflected in price point 
- information based on avg price of quantitative analysts + experience we bring

Other counter arguments: 
- price below our market value (and experience)
- propose: a price at mid point with increase to market value after 2m of work

Strategy: 
- Alignment on what is the price mid point?
- Alignment on what is the price bottom? (anything below is NoGo zone)

bottom: 50 DAI
mid: 60 DAI 

**Not an adhoc analysis, but a framework -> not a set and forget approach**
**It's about scalability of the analysis**
**Loan approaval and pricing under one package**


**Methodology argument:**: 
Pain points: 
- "Your methodology is too complicated" OR "Can you simplify the methodology?"
- "Your methodology is not robust enough"
- "Can you deliver [the amount of work] with this methodology in 1 month?"
- "Can we use the methodology to other collateral application types?" e.g. LINK, SNT etc
- "Why do you need an operational budget for analysis?"

Questions back: 
- "How is this methodology too complex?"
- "How is this methodology not robust enough?"

On operational bduget: 
- We could ask maker for approval before 
- We don't see as source of revenue, simply enabler for analysis. We just pass on expenses incurred at cost. 

Risk assessment: 
- how to come with non-financials assessments? 
> nature is on expert judgement
> hence framework for assessing companies 
> sources and credibility of information

- how are you going to do the simulation? asset pricing? 
> simplified view of the framework 
> estimation of princing in the absence of data 
> path will be simulation. but outcome will be **repetition of framework**

- "Can we use the methodology to other collateral application types?" e.g. LINK, SNT etc
> first part can be left out
> set a new definition for PD for the token. What it means to be in default.  
> look at historical data of token for PD.
> EL, EAD, LGD can be derived from historical data for pricing 
> second part of proposal is relevant: simulation of asset price + pricing estimation

**Proposal review argument (again)**: "It's great but I need a few alterations"

Our questions (for self): 
- How significant is the change? 
- Does it require a full rewrite of proposal or just re-wording of existing?

Questions to ask:
- What is the process for re-submission?
- Does it get through fast approvals if re-submitted? 

*If full re-write:* 
- Option A (preferred): Recommend starting engagement and adapting methodology "on the work" (paid)
- Option B (avoid): Propose a methodology re-write but charged this time.
- Speak of estimating the change prior to committing 

*If partial re-write: wording / minor changes*
Definition: 
- Does not change calculations and core of the methodology steps 
- Extension of methodology to include other collateral types (with limitations)
- Add more detail on other "risk management work"
- *Alterations can be done in hours rather than days of work*

Strategy: 
- Option A (preferred): Recommend starting engagement and adapting methodology "on the work" (paid)
- Option B (2nd best): If really minor, submit amendments within 2 days

## 3. Yes, when can you start (best)

Reasonable: 
- 5 working days
- submit engagement letter for signing by **Monday 1 May**
- At start following **Monday 8 June**

Need to prepare: (**no need to tell Cyrus**)
- engagement letter
- sub-contract agreement
- insurance

**Put in context:** 
- this is a proposal framework 
- details come with progress of work 
- bring expectations down 
- how much science we can put into a framework 

Today:
- morning (phone)

Tomorrow: 
- morning (on phone)


---

# Greetings 

- thanks for making the time 
- give the background: 
    - meeting with Cyrus after first proposal submission
    - team took advice on practical **requirements and priorities** for maker risk team 
    - key themes: collateral onboarding and assist with wider risk work load
    - proposal is result of that conversation

- presentation of the team: 
    - both team members with credit risk management background
    - experience in risk analytics, modelling and system implementation
    - experience in blockchain and involved in the maker community 
    - experience working in the technology start up ecosystem
    - experience shows: able to deal with **both detail of risk analysis and versatility of risk generalists** across changed settings and requirements 

- open discussion for direction from Cyrus

# Setting the scene: 

The problem: 
- Maker requires risk teams to use best practice risk management frameworks to provide quantitative and qualitative assessment on the risks for onboarding new collateral in the portfolio
    + stability fees, liquidation ratios (aka loan-to-value ratio) and debt ceilings
- Versatile and robust approach in managing the Risk workload: 
    + monetary policy, collateral onboarding, general modelling and overall system monitoring

The end goal: 
- The objective of the risk assessment is to provide recommendations on risk parameters settings for these new loan facilities. 

Our objective: 
- Provide risk assessment and due diligence to new collateral applications
- Continuous Risk analytics contributions to enhance the Risk management function

# Collateral onboarding

Four stage process: 
+ Information gathering
+ Credit Risk analysis
+ Credit Risk scoring
+ Risk-weighted analysis & protocol parameters

End goal: 
**developing a systematic and repeatable credit risk framework** for collateral onboarding

- systematic: 
    + can be deployed over different collaterals 
    + can be measured quantitatively across collaterals 
    + can be monitored on the same basis "repetitively"
    + can be managed on a portfolio level systematically

- repeatable: 
    + can be scalable over time ==> even across risk contributors  
    + follows a pattern in the assessment and protocol suggestion
    + provides quantitative trust because is transparent

**Information to credit scoring: GOAL**
+ credit worthiness 
+ financial strength of origination business 
+ CAPACITY to pay investor (debt servicibility)

**Risk-weighted analysis: GOAL**
+ determine optimal protocol setttings => stability fees, liquidation ratios (aka loan-to-value ratio) and debt ceilings
+ account for risk rating + asset collateral characteristics => RISK ADJUSTED protocol suggestions

1. Information gathering
+ company information => financials and non-financials
+ collateral information
+ GOAL: use in credit risk analysis

2. Credit Risk Analysis
+ analysis of financials (company statements) 
    + translation of accounting into credit risk 
    + gauge liquidity, profitability, leverage, coverage and activity
+ analysis of non-financials
    + third party benchmarks, literature studies and expert judgment.

3. Credit Scoring + Credit Rating Master Scale
+ Translate non financial (60%) and financial(40%) into Credit Rating scoring
+ Category attributes (i.e. questions) as well as different weights 
+ Non-financials category are given a 5-point rating scale 
    + Very Positive, Positive, Neutral, Negative, Very Negative, N/A
+ Financials a 3-point rating scale
    + Investment, Sub-Investment, Junk, N/A

**Credit Rating Master Scale**
+ 5 risk ranked ordinal levels => creditworthiness of collateral issuer
+ specific **industry/sub-industry default rate**
    + Industry Probability of Default (PD) based on a combination of literature study, expert judgement and industry benchmark

Map Credit Scoring to Rating Master Scale
+ credit rating score on a 0-100% scale
+ map to Credit Rating Master Scale ==> GOAL: level of creditworthiness
**+ GOAL: gain Adjusted Probability of Default (PD)**

Risk-weighted/ protocol setting
+ Determine Expected Return of collateral onboarding as: 
    + **Expected Return = Expected Gain + Expected Loss**
    + Expected Loss = Adjusted PD x Exposure at Default (EAD) + Loss Given Default (LGD)
    + Expected Gain = (1 - PD) × (NGS + PL × NGL)

Howto: 
 + Monte Carlo simulation to simulate collateral asset price movement
 + **Expected Loss, Expected Gain and the Expected Return** for each price over SF and CR settings 
 + Output: empirical distributions for Expected Loss, Expected Gain and Expected Return

 End goal: 
+ risk parameter settings for the maker protocol

# Continuous risk analytics
Analytics contributions to the maker protocol: 
+ Peer review and validation 
+ Optimise existing monetary policy
+ Review and enrich existing risk modelling
+ Build general risk models and asset specific models
+ Provide explanatory analysis to events

----

# Legal discussion on terms 2020-05-29 (Brian,Jonh,Cyrus)

# Greetings & background

- thanks for making the time to meet (Brian, John and Cyrus)
- have also invited Sarah who my business advisor to this discussion 
- put things into context: 
    - team met with Cyrus around provision of independent risk services
    - the result of those conversations is proposal we submitted for collateral onboarding and assist with wider risk work load
    - this was accepted by the foundation

- My understanding of the ongoing risk work, whcih for the basis of engagement
    - conduct a one month trial with the team to conduct collateral onboarding analysis as a service to Maker
    - following that, engage in an **ongoing service relationship** to provide risk analysis for collateral onboarding & other enhancements to the Maker risk framework **with a revised fee agreed** with Maker

- The terms:
    - For the provision of these services, I submitted an **engagement letter** outlining the services to be provided along with the **terms for provision** of risk services as an independent risk team

I reviewed the grant letter that Cyrus submitted..  
    - **Grantee letter from Maker** as basis of risk services engagement 
    - it does not seem to be structured in a way that is appropriate for **ongoing service provision**

But I reviewed from a commercial perspective. I did not involve a lawyer for legal advice.

I think everybody on the call is keen to get work started
We've put in a lot time and effort to get the proposal going. And we are keen to work with Maker to show the value it can bring. 

But we need to be clear on the legal framework that governs that provision of services
Whilist we have a better understanding of the funding side at your end, considering the type of work that we'll deliver, it feels like the fastest way forward is to amend Scio terms to include your requirements from a grant letter on a Grantor to Grantee relationship. I would like to understand your concerns around amending our terms 


If we have to markup the grant letter...

We need to have the grant letter reviewed by lawyer
There are a number of provisions we need to provide to 

## Scene & problem

    - After review of templated grantee letter, there is a number of outstanding topics that require further understanding on how the mechanism would work in practice

Turn to Brian:
    - Revisit our grantee letter for this grant
    - Relationship is structured, that is, grantor to grantee
    - Talk about how best to work within the grantor to grantee framework

Given background on nature of work, ie risk service, can you please walk us through how the grants program works in practice for this type of service? 

## Topics to cover: 
- General provisions, including jurisdiction
- Liability and its limitations
- Intellectual property
- Warranties
- Payments mechanisms
- Termination mechanisms 
- Confidentiality

## Email from Brian

    - Foundation provides limited services to MakerDAO
    - 18m foundation will no longer exist
    - Independent teams provide services to the DAO. DAO pays from fees
    - Foundation subsidizes teams with grants (interim) to bring project to fruition.
    - Teams have independence of action and decision making 

Intellectual property
    - Independent teams create frameworks 
    - Scio provide materials with disclaimers and warranties
    - Scio maintains intellectual property
    - Scio open sources the framework so community can use/build upon it

- Revisit our grantee letter for this grant
- Relationship is structured, that is, grantor to grantee
- Talk about how best to work within the grantor to grantee framework

---

# Q&A with  Centrifuge

- drop holders: get high yeild
- drop token most stable than tin token
- drop token: interest bearing token
- investor supplies DAI to the tin pool and get drop
- investor redeems DAI + interest after time
- TIN investors can redeem/exit position on a % basis
- DROP investors can redeem at any time

- nav model to price value entire portfolio of loan
- discounted cashflow model  = value of overall portfolio
- tin guarantees at least 10% of the portfolio by TIN token holders
- rebalancing (redemption to token holders) is done by smatrt contracts. 
> If not enough cash, portfolio will redeem by tranches/% of portfolio
> If not enough liquidity, then cash is proportionate split by investors  

how to define parameters in risk: 


- at least 10% of capital supplied by TIN holders (always)
- TIN investor needs to invest first, before any DROP investor
- Loans are guaranteed by those 10%, which allows for further outstanding limit

From centrifuge to maker:
- vault holds DROP tokens and accumulates interest
- oracle gets data from nav model for pricing of collateral
- TIN token holders lose their capital first
- TINLAKE pool own CDP with DROP 

3 layes: 
- TINLAKE pool
- DROP tokens against DAI 
- Maker allows issuance <> MKR would be treated as DROP holders (from a risk perspective)

SF equals the DROP yield
CR (DROP/DAI) would be equal 1:1 
> or LVR of about 90% as TIN guarantees 10% (provision)
> TIN adjusted LVR

when we need close vault/liquidation:
- keeper auction
- keeper gets max outstanding debt amount 
- loss of collateral value may be compensated yield on DROP tokens

- DAI minting is not going to be doing early stage VC capital 
- adjustment of SF, debt ceiling can be during duration
- asset originator can have asset backed in different loan providers


- provision model can have recommendation from risk team
- one term facility but revolving
- 35-50d on avg (ConsolFreight)
- maturity will depend on asset type used as collateral
- more than one pool for same asset can be created, but short term debt 

Monitor: 
- risk class 
- each pool has its own oracle 
- credit rating of individual borrowers, fraud risk



Questions from me: 
- can investors swap the tokens in the market?
- how are the tokens valued? 
- how does monitoring occur? 
- what is the maturity of these loans?
- revolving vs non revolving facility?
- how will LVR adjust provision? (TIN holder capital)
- 
