# Minion Bot - Alpha
Memo API BOT written on Python

Disclaimer.- Minion Bot is currently in alpha. This script is basic, adaptable and can be easily changed to incorporate more commands/functions for the bot. That being said, there will be some bugs that will come about, and these will get ironed out in due time.


# References and Requirements
https://developers.steem.io/tutorials-python/getting_started <br>
https://beem.readthedocs.io/en/latest/installation.html 

# KIS = Keep it simple
Minion bot currently responds to two commands: npost, rpost.

To give minion bot an order, send 0.001 STEEM with a memo using the following format:

(command) (author/permlink) (body) 

  Examples:<br>
  <b>npost</b> This post was made using minion <- Parent Post, not a reply
  
  <b>rpost</b> @meno/working-on-a-minion-bot This is a reply using minion bot <- Reply 
  

# Considerations:
Minion is basically a memo API script that stores all operations on the blockchain, making it's actions recreatable. Because it waits for confirmed blocks, it does have a delay, but it's not too great. 

Currently Minion Bot refunds operator while confirming it obeyed the command, but this could be disabled if need be.


# No Support & No Warranty
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
