import subprocess
def extract_wifi_passwords():
    profiles_data = subprocess.check_output('netsh wlan show profiles').decode('cp437').split('\n')
    profiles = [i.split(':')[1].strip() for i in profiles_data if 'All User Profile' in i]

    for profile in profiles:
        profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear').decode('cp437').split('\n')

        try:
            password = [i.split(':')[1].strip() for i in profile_info if 'Key Content' in i]
        except IndexError:
            password = None
        # print(f'Profile:{profile}\nPassword: {password}\n{"#" * 20}')

        with open(file='wifi_passwords.txt', made='a', encoding='cp437') as f:
            f.write(f'Profile:{profile}\nPassword: {password}\n{"#" * 20}\n')

def main():
    extract_wifi_passwords()

if __name__ == '__main__':
    main()
