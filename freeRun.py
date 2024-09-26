import subprocess,time
try:
    result = subprocess.Popen(
        ['npm','start']
    )
    stdout,stderr = result.communicate()
    print('All Sending Transactions Are Completed')
except subprocess.CalledProcessError as e:
    print('Sendig Transaction Error occured Because of :\n',e)

time.sleep(2)

print('Time To Claim')

time.sleep(2)


try:
    result = subprocess.Popen(
        ['npm','run','claim']
    )
    stdout,stderr = result.communicate()
    print('All Claiming  Are Completed')
except subprocess.CalledProcessError as e:
    print('Claiming Error occured Because of :\n',e)
