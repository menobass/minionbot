from beem.blockchain import Blockchain
from steem import *
from beem import Steem
from beem.account import Account
from beem.comment import Comment

import getpass
import time

# open instances to interact with the steem blockchain
steem = Steem()
blockchain = Blockchain()

def obey(command,blocknum):  # Once Minion receives his orders, he obeys
    print('Obeying my master, his orders are:')
    print(command)
    # Time to slice the memo, first word action npost(new post) rpost(reply to post or comment)
    # For rpost, also extract the author/permanentlink Minion is to reply to
    # the rest of the memo is the body of the post/comment
    memobreak = command
    action = memobreak.split(' ', 1)[0]  # get the first word off the memo, the command

    print('Im performing the action:', action)
    # on this block any command could be coded
    if action == 'npost':
        body = memobreak.split(' ', 1)[1]  # this gets the rest of the memo, it becomes the body
        steem.post("Incubator Post on Block:" + blocknum, body, author=account, tags=["incubator"], self_vote=True)
        print('Post Successfully submitted')
    elif action == 'rpost':
        authorperm = memobreak.split(' ', 2)[1]  # the link to author/permlink is extracted from the memo
        c = Comment(authorperm)
        body = memobreak.split(' ', 2)[2]  # body of the reply
        c.reply(body, title='', author=account, meta=None)  # execute reply
        print('Reply Successfully submitted')
    else:
        print('no recognizable command found, error')

    account.transfer(operator, '0.001', "STEEM", 'Command Executed')  # Respond, Refund
    print('Waiting for new Instructions')

def replay():  # History of account to find missing transactions
    print('Making sure no blocks were missed...')
    log_raw = open("lastblock.log", "r") # open file to check the starting block
    log_block = log_raw.read()
    log_stop = log_block
    print('Las processed Blocks id: ' + log_block)
    for h in account.get_account_history(-1,5):
        if h['_id'] != log_stop:
            if h['type'] == 'transfer' and h['from'] == operator and h['to'] == username:
                print(h)  # block that contains the memo with command
                command = h['memo']
                blocknum = str(h['block'])  # string used to differentiate parent posts
                trans_id = h['_id']
                log = open("lastblock.log","w+") # creates blank log file
                log.write(trans_id) # writes last block's unique id
                time.sleep(3)  # to avoid getting transactions rejected
                obey(command, blocknum)

    print('All caught up, awaiting for commands...')
    stream()  # Back to awaiting commands


def stream(): # Stream Blockchain Realtime
    for op in blockchain.stream():
        if op['type'] == 'transfer' and op['from'] == operator and op['to'] == username:
            print(op)  # block that contains the memo with command
            command = op['memo']
            blocknum = str(op['block_num'])  # string used to differentiate parent posts
            trans_id = op['_id']
            log = open("lastblock.log","w+") # creates blank log file
            log.write(trans_id) # writes last block's unique id
            obey(command, blocknum)


# Main Script Begins
print('This is Minion Bot, It obeys a master operator!')
operator = input('Please enter Operator/Master Account to obey: ')
username = input('Please enter Minion/Slave Account to control: ')
account = Account(username, steem_instance=steem)  # defines account instance
wif = getpass.getpass('Please private Active key for Minion/Slave account: ')

# authenticating the minion account
steem = Steem(keys=[wif])

# Replay or Start from Current Block
start_option = input('Replay from last proccessed Block? y/n: ')
while not(start_option == "y" or start_option == "n"):
    print ('command not recognizned')
    start_option = input('Replay from last proccessed Block? y/n: ')

if start_option == 'y':
    print('Checking for missed Commands...')
    replay()
else:
    print('Minion Bot Ready...')
    print('Waiting for Instructions...')
    stream() # Streaming Blocks, waiting for Memo/Commands from Operator to Minion
