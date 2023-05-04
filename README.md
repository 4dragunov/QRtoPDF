# QRtoPDF
This program takes a PDF template file (which may be a blank page) and creates a multi-page PDF file with QR codes of a specified size from a list of addresses.
## Getting Started

### Prerequisites
Before running this program, make sure you have the following installed:
* Python 3
* qrcode
* PyPDF2

### Installing
To install the required packages, run the following command:
` ` `
pip install qrcode PyPDF2
` ` `
### Usage
To use this program, follow these steps:

Clone this repository.<br/>
Edit the config.py file to set the QR code size and position.<br/>
Add a list of URLs to be converted into QR codes to the urls.txt file.<br/>
Run the program by typing python pdf_qr_generator.py in the command line.<br/>
The resulting PDF file will be saved as output.pdf in the current directory.<br/>

### Configuration

The following variables can be set in the config.py file:<br/>

**'qr_position_x'**: The x-coordinate of the top-left corner of the QR code.<br/>
**'qr_position_y'**: The y-coordinate of the top-left corner of the QR code.<br/>
**'qr_width'**: The width of the QR code.<br/>
**'qr_height'**: The height of the QR code.
Example urls.txt File
```
https://my-site.com/fjfhr7sea
https://my-site.com/4dfu7d+=
...
```
## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

[qrcode](https://pypi.org/project/qrcode/)	<br/>
[PyPDF2](https://pypi.org/project/PyPDF2/)	

