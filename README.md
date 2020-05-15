<center>
  
![](https://img.shields.io/badge/author-Ramesh%20Sachan-brightgreen) ![](https://img.shields.io/badge/licence-MIT-green)

</center>

# InstaSpy!
### Coded by: @holps-7 (https://github.com/holps-7/InstaSpy/)
### Give me the credits if you copy ANY part from this code. Don't be NOOB!!
## Star this repo if you liked the project!

Check out followers and following of any user on Instagram and save them in a CSV file...


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.



### Prerequisites

You will need the following for running this script-<br/>
>1)Python3 installed in your system<br/>
>2)Firefox web browser with Firefox webdriver<br/>
>3)pip3<br/>
>4)selenium<br/>



### Installation Instructions

#### 1) Installing Python3
>Visit the following url for details on how to install Python 3 for various Operating systems https://realpython.com/installing-python/#step-1-download-the-python-3-installer


#### 2) Installing Firefox
```elm
cd
sudo apt-get -y install firefox
cd
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
tar xzf geckodriver-v0.25.0-linux64.tar.gz
sudo mv geckodriver /usr/bin/geckodriver
```


#### 3) Installing pip3
```elm
cd
apt install python3-pip
```


#### 4) Installing Selenium
```elm
cd
pip3 install selenium
```



### Break down into end to end tests

This project is not any kind of extention of any other project



## Deployment

>1. Clone the project<br/>
>2. Follow the installation instructions<br/>
>3. Open InstaSpy.py file in any text editor<br/>
>4. Now, in line 121 replace the following with your credentials and target's username</br>
```elm
('<Username>', '<Password>', '<target_username>')
```
>7. Open terminal and run the following command<br/>
```elm
cd Downloads/InstaSpy-master
python3 InstaSpy-script.py
```
>8. Wait for around 5 minutes and let the script run<br/>
>9. After successful execution of the script Firefox will close and now you can check 'InstaSpy-master' folder, it will have two .csv files-<br/>
>>**followers.csv**    This file will contain list of all the followers of target<br>
>>**following.csv**    This file will contain list of all those who follow target (following)<br/>

    PS:- I used Atom editor, which is one of the greatest editors.
         Availabe for free on https://atom.io

## Contributing

Feel free to create Pull Requests, for contributing.


## Authors

  * **Ramesh Sachan** - Vellore Institute of Technology

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



## Legal disclaimer:

**Usage of InstaSpy for attacking target without prior mutual consent OR flooding 'Instagram.com' with requests is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program. Only use for educational purposes.**
