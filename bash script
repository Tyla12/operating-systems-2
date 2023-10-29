#!/bin/bash
echo "NGINX CONFIG SCRIPT"
echo "####################"
echo "Script is starting..."

sleep 1

#checks if Nginx is installed and if not , it installs it
if command -v nginx >/dev/null 2>&1; then
   sleep 1
   echo "Nginx is not installed. Installing Nginx..."
   sudo apt-get update
   sudo apt-get -y install nginx
   echo "Nginx has been installed."
else
   sleep 1
   echo "Nginx is already installed, continue with configurations"
fi

#prompts the user for the directory name and path
read -p "Enter the directory name: " dir
sleep 1
read -p "Enter the directory path (e.g /var/www/html/): " path

#checks if the directory exist and removes its information
if [-d "$path/$dir" ];then
    echo "Directory $dir already exist. Deleting it's information"
    sleep 1
    sudo rm -rf "$path/$dir"
    echo "Directory cleared"
fi

#creates the directory
echo "Creating directory $dir at $path"
sleep 1
sudo mkdir -p "$path/$dir"
sleep 1
echo "Directory created"

#prompts user for their usernae
read -p "Enter your username: " username

#Changes ownership to the user provided
echo "Changing ownership of $dir to $username"
sleep 1
sudo chown "$username":root "$path/$dir"
sleep 1
echo "Ownership has been changed to $username"

#Creates a symbolic link
echo "Creating symbolic link"
sleep 1
sudo ln -s "$path/$dir" "$dir"
sleep 1
echo "Symbolic link has been created"

#Creates and fills the testpage
echo "Creating test index.html"
sleep 1
echo "Adding dummmy content to test index.html"
sleep 1
cd "$dir" || exit
echo "<html><body><h1>This is my bash script</h></body></html>" > "index.html"
cat "index.html"
echo "Content added"
sleep 1

echo "End of script"


