![ screenshot ](https://github.com/offiicialkamal/tools-organizer/blob/main/Screenshots/Screenshot%20(1).png)
# Desclaimer

The tool is designed for developers, who have lots of tools but all are in seprate repositories. this tool helps to organize all the tools in a single place with a minimal efforts.


# Usage

  - fork the repository
  - open and edit the `settings.json`

```
pkg install git -y
git clone https://github.com/offiicialkamal/tools-organizer.git
cd tools-organizer
pip install -r requirements.txt
python main.py
```

> [!NOTE]
> fully edit the settings.json and for more security use any encryption tool like <a href="https://github.com/hackesofice/Encrypt-python.git" target="_blank"> this <a> to encrypt your files if needed
> this file is responsible for the all other things
---

# Expected your Projects Structure

This tool looks for a module called `your-project.main` which is an entrypoint of your tools
example file structure -
```
  your-project/
  ├── main.py OR main.cpython-3xx.so 
  ├── __init__.py  # must add ( Blank / with content )
```  

---

## LICENSE
The project is relased under <a href="/LICENSE"> MIT LICENSE </a> 

## SUPPORT 
found any bug or have any suggetions ? don't warry just open a issue <a href="https://github.com/offiicialkamal/tools-organizer/issues"> hear </a> we are waiting for any small suggetions / bugs and well resolve it as soon  as posssible  


## CONTRIBUTION

I Love contributions if youre an developer and wanna add / improve this project please add an clear description about that specific fix / improvements well merge your PRs if we found it usefull, your small contributon may help us to improve the project



