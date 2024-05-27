import random
import string
import time
import requests
from config import DELAY


# ФУНКЦИЯ ГЕНЕРАЦИИ USERNAME (пару слов слитно и 4 цифры)
def generate_username():
    username = ''.join(random.choices(words_for_nick, k=2)) + ''.join(random.choices(string.digits, k=4))
    return username


# ФУНКЦИЯ РАНДОМНОЙ ЗАДЕРЖКИ
def random_sleep():
    # Генерируем случайную задержку в заданном интервале с округлением до одной десятичной цифры
    delay = round(random.uniform(DELAY[0], DELAY[1]), 1)
    print(f'   sleep {delay}..')
    # Выполняем задержку
    time.sleep(delay)


# ФУНКЦИЯ СМЕНЫ IP У МОБИЛЬНОЙ ПРОКСИ
def change_ip(proxy_links):
    while True:
        link = random.choice(proxy_links)
        response = requests.get(f'{link}&format=json')
        if response.status_code == 200:
            # Извлекаем новый IP-адрес из ответа
            new_ip_data = response.json()
            new_ip = new_ip_data.get('new_ip')

            if new_ip:
                print(f'New IP: {new_ip}')
                return True
            else:
                print('Failed to extract new IP from response')
                return False
        else:
            print(f'Failed to change IP: {response.text}')
            return False


# ФУНКЦИЯ ОТПРАВКИ УВЕДОМЛЕНИЯ В ТЕЛЕГРАМ
def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, json=params)
    if response.status_code == 200:
        print("Сообщение успешно отправлено в телеграм-чат.\n\n")
    else:
        print("Произошла ошибка при отправке сообщения в телеграм-чат.\n\n")


words_for_nick = [
    "bitcoin", "ethereum", "blockchain", "cryptocurrency", "wallet", "mining", "hash", "node",
    "decentralized", "ledger", "transaction", "privatekey", "publickey", "consensus", "smartcontract",
    "altcoin", "ico", "token", "exchange", "fork", "gas", "solidity", "proofofwork", "proofofstake",
    "satoshi", "airdrop", "hodl", "whale", "fomo", "fud", "trading", "marketcap", "supply", "block",
    "confirmation", "address", "seedphrase", "coldstorage", "hotwallet", "defi", "dex", "yieldfarming",
    "staking", "governance", "oracle", "scalability", "interoperability", "sharding", "layer2",
    "sidechain", "lightningnetwork", "privacycoin", "mempool", "gasfee", "dapp", "stablecoin",
    "nft", "metaverse", "hashrate", "difficulty", "cryptographic", "peertopeer", "merkletree",
    "cryptography", "burn", "pump", "dump", "moon", "bagholder", "whitepaper", "utilitytoken",
    "securitytoken", "dao", "crosschain", "atomicswap", "rebase", "impermanentloss", "flashloan",
    "liquiditypool", "amm", "rugpull", "faucet", "testnet", "mainnet", "airdrop", "ico", "ido",
    "ieo", "sto", "whitelist", "premine", "blockexplorer", "doublespend", "halving", "node",
    "validator", "beaconchain", "custodial", "noncustodial", "coldwallet", "hotwallet",
    "hardwarewallet", "paperwallet", "seedphrase", "brainwallet", "gaslimit", "gasprice",
    "txid", "txfee", "txpool", "timestamp", "difficultyadjustment", "blockreward",
    "blockheight", "blocktime", "nonce", "coinbasetransaction", "orphanblock", "uncleblock",
    "atomicswap", "coloredcoins", "multisig", "lightwallet", "layer1", "layer2",
    "paymentchannel", "statechannel", "offchain", "onchain", "rollup", "zeroknowledgeproof",
    "zksnark", "zkstark", "privacypreserving", "anonymity", "fungibility", "nonfungible",
    "cryptoeconomics", "cryptonomics", "supplyanddemand", "gametheory", "economicincentive",
    "stakeholder", "validator", "delegator", "epoch", "slashing", "rewards", "inflation",
    "deflation", "treasury", "governance", "proposal", "voting", "quorum", "consensusmechanism",
    "bft", "pbft", "dbft", "consensusalgorithm", "finality", "latency", "throughput",
    "blockpropagation", "networkeffect", "metcalfeslaw", "distributedledger", "dlt",
    "permissioned", "permissionless", "trustless", "sybilattack", "attack", "reorg",
    "mev", "frontrunning", "backrunning", "sandwichattack", "flashbot", "validatorset",
    "stakingpool", "delegatedstaking", "bonding", "unbonding", "redelegation",
    "slashingcondition", "networkupgrade", "hardfork", "softfork", "contentiousfork",
    "chainsplit", "chainmerge", "consensusfork", "protocolupgrade", "backwardcompatibility",
    "forwardcompatibility", "protocol", "protocollayer", "baselayer", "scalabilitytrilemma",
    "security", "decentralization", "scalability", "trilemma", "validatoreconomics", "validatorrewards",
    "consensus", "algorithm", "blockchaintechnology", "distributed", "ledgertechnology",
    "peer", "transactions", "network", "hashing", "public", "private", "keys", "crypto",
    "exchange", "trading", "platforms", "market", "capitalization", "tokens", "forks",
    "protocols", "smart", "contracts", "defi", "decentralized", "finance", "liquidity",
    "mining", "proof", "work", "stake", "validators", "nodes", "governance", "mechanisms",
    "decentralized", "autonomous", "organizations", "daos", "consensus", "mechanisms",
    "proof", "work", "pow", "proof", "stake", "pos", "delegated", "pos", "dpos",
    "byzantine", "fault", "tolerance", "bft", "privacy", "coins", "zcash", "monero",
    "dash", "anonymity", "mixers", "coinjoin", "zk", "snarks", "sidechains",
    "lightning", "network", "scalability", "solutions", "state", "channels", "rollups",
    "optimistic", "rollups", "zk", "rollups", "layer", "solutions", "interoperability",
    "bridges", "cross", "chain", "swaps", "atomic", "swaps", "wallets", "hardware",
    "wallets", "ledger", "nano", "trezor", "software", "wallets", "metamask", "trust",
    "wallet", "mobile", "wallets", "desktop", "wallets", "cold", "storage", "hot",
    "storage", "custodial", "wallets", "noncustodial", "wallets", "mnemonic", "phrases",
    "seed", "phrases", "public", "addresses", "private", "keys", "multisignature",
    "wallets", "hardware", "security", "hardware", "wallets", "hardware", "wallets",
    "ledger", "nano", "trezor", "keepkey", "software", "wallets", "mobile", "wallets",
    "desktop", "wallets", "exchange", "wallets", "custodial", "wallets", "noncustodial",
    "wallets", "seed", "phrases", "mnemonic", "phrases", "brain", "wallets", "paper",
    "wallets", "transaction", "fees", "gas", "fees", "block", "rewards", "mining",
    "rewards", "staking", "rewards", "inflation", "rewards", "treasury", "rewards",
    "consensus", "mechanisms", "proof", "work", "proof", "stake", "delegated", "proof",
    "stake", "byzantine", "fault", "tolerance", "governance", "mechanisms", "voting",
    "systems", "dao", "proposals", "onchain", "governance", "offchain", "governance",
    "staking", "delegating", "validators", "delegators", "bonding", "unbonding",
    "redelegating", "validators", "slashing", "conditions", "epoch", "rewards",
    "inflation", "deflation", "treasury", "proposals", "governance", "quorums",
    "finality", "latency", "throughput", "block", "propagation", "network", "effects",
    "metcalfes", "law", "distributed", "ledger", "technology", "permissioned",
    "permissionless", "systems", "trustless", "systems", "sybil", "attacks", "reorg",
    "mev", "front", "running", "back", "running", "sandwich", "attacks", "validators",
    "staking", "pools", "delegated", "staking", "bonding", "unbonding", "redelegating",
    "slashing", "conditions", "network", "upgrades", "hard", "forks", "soft", "forks",
    "contentious", "forks", "chain", "splits", "chain", "merges", "consensus", "forks",
    "protocol", "upgrades", "backward", "compatibility", "forward", "compatibility",
    "protocol", "layers", "base", "layers", "scalability", "trilemma", "security",
    "decentralization", "scalability", "trilemma", "validator", "economics", "validator",
    "rewards"
]
