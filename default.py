import mintapi

email = 'camille.h.walters@gmail.com'
password = 'FMScnps7^'

mint = mintapi.Mint(
email, password,  # Your password used to log in to mint
# Optional parameters
mfa_method='sms',  # See MFA Methods section
                   # Can be 'sms' (default), 'email', or 'soft-token'.
                   # if mintapi detects an MFA request, it will trigger the requested method
                   # and prompt on the command line.
mfa_input_callback=None,  # see MFA Methods section
                          # can be used with any mfa_method
                          # A callback accepting a single argument (the prompt)
                          # which returns the user-inputted 2FA code. By default
                          # the default Python `input` function is used.
mfa_token=None,   # see MFA Methods section
                  # used with mfa_method='soft-token'
                  # the token that is used to generate the totp
intuit_account=None, # account name when multiple accounts are registered with this email.
headless=False,  # Whether the chromedriver should work without opening a
                 # visible window (useful for server-side deployments)
                     # None will use the default account.
session_path=None, # Directory that the Chrome persistent session will be written/read from.
                   # To avoid the 2FA code being asked for multiple times, you can either set
                   # this parameter or log in by hand in Chrome under the same user this runs
                   # as.
imap_account=None, # account name used to log in to your IMAP server
imap_password=None, # account password used to log in to your IMAP server
imap_server=None,  # IMAP server host name
imap_folder='INBOX',  # IMAP folder that receives MFA email
wait_for_sync=False,  # do not wait for accounts to sync
wait_for_sync_timeout=300,  # number of seconds to wait for sync
fail_if_stale=True, # True will raise an exception if Mint is unable to refresh your data.
use_chromedriver_on_path=False,  # True will use a system provided chromedriver binary that
                                 # is on the PATH (instead of downloading the latest version)
driver=None        # pre-configured driver. If None, Mint will initialize the WebDriver.
)

# Get account information
mint.get_account_data()
print("here")

# Get budget information
mint.get_budget_data()

# Get transactions
mint.get_transaction_data() # as pandas dataframe

# # Get transactions for a specific account
# accounts = mint.get_account_data()
# for account in accounts:
#     mint.get_transaction_data(id=account["id"])

# Get net worth
mint.get_net_worth_data()

# Get credit score
mint.get_credit_score_data()

# Get bills
mint.get_bills()

# Get investments (holdings and transactions)
mint.get_investment_data()
#
# Close session and exit cleanly from selenium/chromedriver
mint.close()

# Initiate an account refresh
mint.initiate_account_refresh()

# you can also use mintapi's login in workflow with your own selenium webdriver
# this will allow for more custom selenium driver setups
# one caveat is that it must be based on seleniumrequests currently
# seleniumrequests has most browsers already
# it also has mixins for any browsers it doesn't have so the sky is the limit!
from seleniumrequests import Firefox
mint = mintapi.Mint()
mint.driver = Firefox()
mint.status_message, mint.token = mintapi.sign_in(
email, password, mint.driver, mfa_method=None, mfa_token=None,
mfa_input_callback=None, intuit_account=None, wait_for_sync=True,
wait_for_sync_timeout=5 * 60,
imap_account=None, imap_password=None,
imap_server=None, imap_folder="INBOX",
)
# now you can do all the normal api calls
# ex:
mint.get_transaction_data()
