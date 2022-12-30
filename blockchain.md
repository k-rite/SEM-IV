# Introduction to Blockchain Technologies

## Date: 30/12
## Centralized Ledger and Distributed Ledger
![Centeralised-Distributed](https://i.imgur.com/ocYZMge.jpg)
### Centralized Ledger
- Ledger is a book of record keeping, All the financial transaction of the organization.
- A Central Ledger also known as General ledger,
- It contains all the accounts for recording transactions related to company assets, liabilities, revenue and expenses.
- Every financial transaction needs a ledger
- Nowadays computerized ledger came into existence that is ERP
- The general ledger works as a central repo for accounting data, transferred from all sub-Ledgers, cash management, fixed assets, purchasing and projects.
- The general ledger is the backbone of any accounting system which holds financial and non-financial data for an organization.
- The collection of all account is known as general ledger.
- Example: Bank has total control over which transactions are posted on the ledger because it is centralized asset ledger which list all transactions that is controlled by a single entity such as a bank statement.
- The Centralized ledger can be risky, if the entity in charge has malicious intent, It can damage to its clients.
- Another disadvantage of the Centralized ledger is the controlling entity can shut down without notice and transaction will no longer be processed.
### Distributed Ledger
- A distributed ledger is an assets' database that can be shared across the network of multiple sites, geography or institutions.
- All participants in the network can have their own identical copy of the Ledger.
- Any changes to the ledger are reflected in all copies within seconds or minutes.
- The asset can be financial, legal, physical or electronic.
- The security and accuracy of all the assets is stored in the ledger are maintained cryptographically.
- Two parties are able to make an exchange without the oversight or intervention of 3rd party
- Users are in control of their information and transaction.
- Data is complete, consistent, timely, accurate and widely available
- Due to decentralized network, Blockchain does not have a Central point of failure and is able to withstand malicious attacks.
- Users can trust that transactions will be executed exactly as the protocol commands, Removing the need for a trusted 3rd party

## Permissionless and Permissioned Blockchain
![Permission and Permissionless](https://www.foley.com/en/insights/publications/2021/08/-/media/images/insights/publications/2021/08/22mc35029-blockchain-graphic--permissions06.png)
- Permissionless blockchain allows any user to anonymously join the Blockchain network and do not restrict the rights of the nodes on the Blockchain network.
- In permissioned Blockchain Restrict access to the network to certain nodes, and it may also restrict the rights of those nodes on that network.
- The identities of the users of a permissioned blockchain are known to the other users of that permissioned blockchain.

## Types of Blockchain
### Public Blockchain
- Public Blockchain are permissionless in nature, allows anyone to join and are completely decentralized.
- They allow all nodes on the blockchain to have equal rights to access the blockchain, create new blocks of data and validates blocks of data.
- It is the non-restricted form of ledger in which each peer has a copy, The user has access to historical and contemprory records and the ability to perform mining operations.
- The complex computations must be performed to verify transactions and add them to the ledger.
- In this Blockchain, No transaction maybe altered.
#### Advantages
- Trustable:
    - The nodes within this Blockchain do not need to know or trust each other because the pow procedure ensure no fraudulent transaction.
- Secure
    - It can have as many participants making it a secure network
#### Disadvantages
- Lower tps:
    - The number of transactions per second in the public blockchain is extremely low. Because the network is too large, it takes time to verify a transaction and do pow.
- Scalability
- Here the transactions are processed and completed slowly, This humps scalability. Because the more we try to expand the network size and slower it will become.

#### Usage of Blockchain
- Voting
- Fund raising

### Private Blockchain
- Private Blockchain are referred to as permissioned Blockchain controlled by a single organisation.
- The centeral authority determines who can be a node
- It also grant each node with equal rights to perform function.
- They're often a small network within an organization

#### Advantages
- Speed
    - The transaction here are faster, Since the private network has smaller number of nodes which shortens the time to verify a  transaction.
- Scalability
    - The private blockchain can be scalable as the companies allow to easily raise or decrease the network size.

#### Disadvantages
- Centralization
    - They require a Central identity and access management system to function. This system provides full administrative and monitoring access to capabilities.
- Lower security
    - The network has few nodes, so it is more harm to a security compromise

#### Usage
- Supply chain management
- asset ownership

### Hybrid Blockchain
- They are controlled by a single organization but with a level of oversight performed by the public blockchain which is required to perform certain transactions' validation 
- It enables enterprises to contract a private permission based system alongside a public permissionless system allowing them to choose who has access to certain blockchain data and what data is made public.
- Transaction are not made public easily, but they can be validated by granting access to smart contracts.
#### Advantages
- Secure
    - This Blockchain operated within a closed environment preventing outside hackers for 50% attack on the network.
- Cost-effective
    - Transaction are inexpensive and scalable better than public blockchain.

#### Disadvantages
- Lack of transparency
    - Since the information can be hidden, This type of blockchain isn't completely transparent.

#### Usage
- Real Estate
- Retail Management
----------

### Consortium Blockchain
- They are permissioned Blockchains governed by a group of organization rather than one entity.
- It involves various organizational members working together on a decentralized network.
- Pre-determined nodes control the consensus methods
- It has a validator node for initiating, receiving and validation transactions.
- Transactions can be initiated or received by a member node
#### Advantages
- Secure
    - This blockchain is more secure, scalable and efficient than a public blockchain

#### Disadvantages
- Lack of transparency
    - This blockchain has lower degree of transparency if the member node is deeply linked and if it's attacked it can the whole network inoperable.
#### Usage
- Research
- Food tracking

----------

## DATE: 23/12

## Symmetric and Asymmetric Encryption

### Asymmetric Encryption
![Symmetric Key](https://www.ssl2buy.com/wiki/wp-content/uploads/2015/12/Symmetric-Encryption.png)

- A sends message to B using B's public Key
    - A signs the message, A's private key
- Encrypted email to B
- Blockchain
    - Verification of A's transaction
    - b decrypts the message using B's private key
- B receives the message

A wants to send B some bitcoin,
First A needs to get B's Public address, A then signs the message with his private key to ensure the transaction has been modified
the transaction is then encrypted and verified.
B would then decrypt the message using B's private key and access the message
A public key allows you to receive cryptocurrency transactions, It is a cryptographic code that is paired to private key.
While anyone can send transaction to the public key whereas the private key is used to unlock the transaction and proves that 
you are the owner of the message that received the transaction


## Principles of Blockchain
1. Network integrity
    - The Basic Principle:
        - Since the blockchain is spread over thousands of computers, It is networked and the participants in the blockchain economy, Maintain integrity as every interaction is indelibly(Can't be deleted) recorded
    - The Problem Solved
        - Over the internet we need intermediate parties to solve the integrity problem, Thou you can share data, files, photos etc. easily over the internet, The same doesn't hold for the money because there's a risk of double spending.
    - Breakthrough
        - The BlockChains offers consensus mechanism to solve the double spending problem through the timestamping of the first transaction and all the transactions thereon. In addition, the pow mechanism to ensure integrity over the blockchain.
    - Implications
        - For the first time ever, We have a platform that ensures trust in the transaction and recorded information, No matter how the other parties acts.
2. Distributed Panel
    - Basic principle:
        - No one person or organization has outsized(large) control over the whole or access to an outsized amount of data.
    - Problem to be Solved:
        - Big Organization or Central powers have been proven time and again that they can use the power of data without the users knowledge and implement large scale changes without the users consent
    - Breakthrough
        - Blockchain means mass collab at its best, The user has the power over their data and the level of participation. Every transaction is broadcasted to everyone. Nothing is with the Central third party or central server.
    - Implication
        - A platform to enable distributed models of wealth creation, A p2p collab to transfer real powers to the citizens.

3. Value as incentive
    - Basic Principle
        - A blockchain is designed to incentivize its users and people who want to hold on to these incentives 
    - Problem to be solved
        - Improper use of data because of invariable incentives received over the dot com era, People who receive the incentive do not worry weather the data gets leaked because it is the customer who ultimately suffers 
    - Breakthrough
        - The extreme resources requirement and the reward mechanism ensure that participants to the right thing.
    - Implications
        - The internet era do not punish the offenders in any way but on Blockchain Social Media they can lose the reputation score for bad behavior
4. Security
    - Basic Principle
        - The use of cryptography is efficient and provides authenticity and confidential 
    - Problem to be solved
        - Hacking, Identity theft, fraud, phishing, spam. The current reliance on strong passwords because the service provider is not responsible for our safety. In the next stage of digital revolution involves communicating money directly between multiple parties then communication need to be hack proof
    - Breakthrough
        - Public and private key infrastructure, The Blockchain runs on a very well-known and established SH256 algorithm.
    - Implication 
        - A secure design that is transparent and protect what happens to our data. 
5. Privacy 
    - Basic Principle:
        - People get to be in complete control of their data.
    - Problem to be solved
        - Collecting and using our data without our understanding and permission, It doesn't ensure protection from hackers
    - Breakthrough
        - On a Blockchain you need not provide an identity, Since the software is open source it is unnecessary to store the data and use it for marketing 
    - Implication
        - Data is private, and you own it
6. Rights Reserved
    - Basic Principle
        - Ownership rights are transparent and enforceable. Individual freedoms are recognized and respected.
    - Problem to be Solved
        - Authorities or software blocking privacy and online rights, Intermediate parties and the cost attached 
    - Breakthrough
        - Smart Contract which allows for transaction to proceed only when pre-defined benchmarks are having reached and agreed upon on all parties.
    - Implication
        - Clarity, Enforcement and correct usage of assets rights on the Blockchain economy.
7. Inclusion
    - Basic Principle
        - The economy works best where it works for everyone which lowers the barriers for participants 
    - Problem to be Solved
        - A large population on earth is still excluded from the internet and the financial system, hence need economic opportunities.
    - Breakthrough
        - Blockchain works over the internet, but they can work without it too, There is no bank accounts, proof of citizenship, no stable currency is required
    - Implication
        - The foundation of prosperity is inclusion and Blockchain helps it



----------

## DATE: 16/12

- Records information
- Distributed Ledger
- Decentralized P2P
- Chain of blocks
- NONCE (Number used only once)
- Double Spending
- P-O-W (Proof of Work)
- Mining

SH56 - Algorithm
Smart Contracts
Genesis Block - First Block | No prev block

![Memory - Miners](https://miro.medium.com/max/700/0*UBB7E4EX08OkZy6Z.jpg)


----------


## What is Blockchain?
- Blockchain is a shared immutable ledger that facilitates the process of recording transactions and tracking asserts in a business network.
- An asset can be tangible (A house, car, cash,) or in-tangible (property, copyrights, branding)
- A Blockchain is a hash linked Data Structure 
- It is a chain of or records stored in the form of Blocks, which are controlled by 'no-single authority'
- Once an information stored in the blockchain, It is extremely difficult to change or alter it.
- Each transaction in a blockchain is secured with a digital signature that proves its authenticity.
- Due to use of encryption and digital signatures the data stored on the blockchain is tamperproof and cannot be changes.
- It is a distributed ledger that is completely open to any and everyone in the network.

## Importance of Blockchain to Businesses
- Immutability - Data once stored cannot be modified or alter.
- Transparency - It offers transparency so that businesses can track every system detail
- Efficiency - It enables the Business to carry out, Operations efficiently
- Traceability - Offer all time traceability that prevents fraudulent activities
- Security - Utilizes high level cryptography algorithm and methods


## Core that Blockchain will impact
- Supply chain - Improves transparency, Traceability and removes any fraud activities
- Finance - Helps Streamline processes, offers authenticity and economic benefits
- Healthcare - Unique patient data, drug traceability, clinical trials and data security
- Retail - Better inventory management, faster settlements and less paper work


## Key Features of Blockchain
- Immutability - Information within a block can't be altered without producing a change in the subsequent block.
- Distributed Ledgers - It records the transaction such as exchange of assets or data among the participants in the network. It is the type of database that is shared, replicated and synchronized among the participants of a decentralized network.
- Data Security - Blockchain uses cryptography to add a layer of security to the data stored on the network.
It utilizes complex mathematical algorithms that were used to secure the data and systems on the blockchain network. Also, each block on the network carries unique hash which means that no data can be forced or changed by hackers
- Decentralization - The entire blockchain is shared among all the computer of the network, Hence no single authorities controls it.
- Smart Contracts - It helps companies to manage business contracts without the need of third part they are programmed stored blockchain system that run automatically when pre-determined conditions are met. Example a logistics company can haves mart contract that automatically makes payment once Woods have arrived at the port.
- Consensus - A blockchain system establishes rules about participants consent for recording transaction, You can record new transactions only within the majority of the participants in the network, give the consent. A proof of work is requirement that expensive computation can be performed in order to facilitate the transactions. POW exists to enable trustless consensus 
- Mining - it means adding transaction records to the blockchain ledger after confirming the validity of the transaction. It involves using complex hardware to perform mathematical calculations in order to verify transactions.
Computer miner verify the validity of transactions and only then put them into a secure block. 
These blocks combine to form a blockchain. After creating a new hash for every secure block miners are rewarded financially. Mining is needed so that bitcoins are not double spent
- Quick Settlement - traditional banking system is quite slow. Transaction takes days to process after the settlement whereas Blockchain transaction are settled in a short time.
- NONCE - A Nonce in a blockchain is a whole number that is randomly generated when a block is created, which then generates a block header hash.
- NODE - Every participant who runs a computer that contributes to the network also known as node. Node maintains their own copy of blockchain and constantly checks with other nodes to make sure everyone has the same record of data
- Double Spending - Sending a Bitcoin transaction to two different recipients at the same time is called double spending. This must be avoided at all cost.
- Block - Transactions are combined into single Blocks and every 10mins a new block of 1 MB size of block is created, Every block contains 4 
1. Timestamp(Ref to prev block), 
2. Hash Value(Summary of transaction, 
3. Secure Hashing implies that editing a block without causing a change in the subsequent block is impossible), 
4. Peer to Peer (A highly interconnected network which shows interaction that happened between two peers))

## Working of Blockchain
1. Suppose two users in a blockchain network A and B wants to create a new transaction, A sends 5 BTC to B, They will request the transaction to be mined.
2. The transaction can take place if all other participants in the network verify it as a genuine transaction
3. The data of the transaction requires a hash value to process the transaction each of the participants will check certain information above the transaction such as A has sufficient funds to make the transaction.
4. Once the verification is complete, the transaction is ready to take place Not the transaction is added into memory pool of blockchain.
5. The created block is added to the Existing blockchain. Every new block has a Block header which is consists of Timestamp, hash value, prev harsh and transaction data summary. Every Block has a unique has value which acts like a signature.
6. The Block is mined with the help of Hash function, After this the transaction is completed and money is sent to B.
![Working of Blockchain](https://i.imgur.com/ny5x6vf.jpg)
----------

