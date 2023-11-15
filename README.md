# noGenEmailer - Automated Email Sender

noGenEmailer is a Python-based Automated Email Sender that allows you to send personalized emails to a list of contacts. It's suitable for various businesses, including E-commerce sites, Hospitals, Schools, etc.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/noGenEmailer.git
   cd noGenEmailer

2. Install dependencies:

   ```bash
   pip install requirements.txt

3. Set up your environment variables:
   Create a `.env` file in the root directory and add the following:

   ```env
   SMTP_USERNAME=your_gmail_username@gmail.com
   SMTP_PASSWORD=your_gmail_app_password
   SENDER_EMAIL=your_sender_email@gmail.com

4. Prepare your CSV file:
   The main program file can be recustomized to suit your personal needs as currently we have three 
   columns and that is; `FirstName`, `LastName` and `Email`. If your CSV file has more, improving the 
   iteration cycle and use of Jinja2 conditionals can be really helpful

4. To the folder of templates:
   Add your customized templates

5. Run the application:

   ```bash
   python3 programmeName.py

## Features

- Personalization: Send personalized emails using contact information    from the CSV file.
- Customizable Template: Easily modify the HTML template to suit your branding.
- SMTP Configuration: Configure your SMTP server details via environment variables.

## Contact
For questions or support, please contact Dharren Pius Makoha at `dharrydharrenzera@gmail.com.`
