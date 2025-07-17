# Birthday Wisher 🎉

Birthday Wisher is a Python project that automatically sends personalized birthday emails to people listed in a CSV file. It uses customizable letter templates and securely handles email credentials via environment variables.

## Features

- Reads birthday data from a CSV file
- Sends personalized birthday wishes using random letter templates
- Uses Gmail SMTP for sending emails
- Securely loads email credentials from a `.env` file
- Easy to customize and extend

## Project Structure

```
.env
.gitignore
birthdays.csv
main.py
Readme.md
letter_templates/
    letter_1.txt
    letter_2.txt
    letter_3.txt
```

- **main.py**: Main script for sending birthday emails.
- **birthdays.csv**: List of people and their birthdays.
- **letter_templates/**: Folder containing birthday letter templates.
- **.env**: Stores your email credentials (not tracked by git).
- **.gitignore**: Ensures `.env` is not committed.
- **Readme.md**: Project documentation.

## Setup

1. **Clone the repository**

   ```sh
   git clone <your-repo-url>
   cd Birthday\ Wisher
   ```

2. **Install dependencies**

   ```sh
   pip install pandas python-dotenv
   ```

3. **Configure your email credentials**  
   Create a `.env` file in the project root:

   ```
   EMAIL=your_email@gmail.com
   PASS=your_email_password_or_app_password
   ```

   > **Note:** For Gmail, you may need to use an [App Password](https://support.google.com/accounts/answer/185833) if 2-Step Verification is enabled.

4. **Add birthdays**  
   Edit `birthdays.csv` and add entries in the format:

   ```
   name,email,year,month,day
   John,john@example.com,1990,6,14
   ```

5. **Customize letter templates**  
   Edit or add files in `letter_templates/` using `[NAME]` as a placeholder for the recipient's name.

## Usage

Run the script:

```sh
python main.py
```

- If today matches any birthday in `birthdays.csv`, an email will be sent using a random template.

## How It Works

- The script checks today’s date against entries in `birthdays.csv`.
- If a match is found, it selects a random template from `letter_templates/`.
- The `[NAME]` placeholder in the template is replaced with the recipient’s name.
- An email is sent via Gmail SMTP.

## Example

Suppose `birthdays.csv` contains:

```
name,email,year,month,day
Manish,manishmaurya9172@gmail.com,2003,6,14
```

On June 14th, the script will send a birthday email to Manish using one of the templates.

## License

This project is for educational purposes.

## Author

Manish
