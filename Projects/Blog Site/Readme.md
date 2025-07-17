# Bloggy - A Modern Blog Site

Bloggy is a responsive blog website built with Flask and Tailwind CSS. It features dynamic blog posts, a contact form with email notifications, and a clean, modern UI. This project demonstrates full-stack web development using Python, HTML, CSS, and JavaScript.

## Features

- **Home Page:** Lists all blog posts fetched from an external API.
- **Individual Post Pages:** Displays full content for each blog post.
- **About Page:** Static page describing the author.
- **Contact Page:** Users can send messages via a form; messages are emailed to the site owner.
- **Responsive Design:** Uses Tailwind CSS for mobile-friendly layouts.
- **Sticky Navigation:** JavaScript-powered navbar for improved UX.
- **Social Media Links:** Footer includes social icons.

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, Tailwind CSS, JavaScript
- **Email:** SMTP via Gmail (requires app password)
- **Environment Variables:** Managed with `.env` and `python-dotenv`
- **API:** Blog posts loaded from [npoint.io](https://api.npoint.io/c790b4d5cab58020d391)

## Project Structure

Blog Site/ ├── main.py\
├── .env \
├── package.json\
 ├── static │ ├── assets/ │
│ ├── favicon.ico │ │ └── img/ │ ├── css/ │ │ ├── styles.css │ │ └── output.css │ └── js/ │ └── scripts.js\
 ├── templates/ │ ├── index.html │ ├── post.html │ ├── about.html │ ├── contact.html │ ├── header.html │ └── footer.html └── Readme.md

## Getting Started

### Prerequisites

- Python 3.7+
- Node.js (for Tailwind CSS compilation)
- Gmail account (for contact form email)
- [pipenv](https://pipenv.pypa.io/) or `pip` for Python dependencies

### Installation

1. **Clone the repository:**

   ```sh
   cd bloggy
   ```

2. **Install Python dependencies:**

```sh
  pip install flask requests python-dotenv
```

3. **Install Node.js dependencies (for Tailwind CSS):**

```sh
  npm install
```

4. **Set up your .env file:**

```sh
 MYUSER=your_gmail@gmail.com
PASS=your_gmail_app_password
PERSON=recipient_email@gmail.com
```

5. **Compile Tailwind CSS (optional, if you want to customize styles):**

```sh
  npx tailwindcss -i [styles.css](http://_vscodecontentref_/12) -o [output.css](http://_vscodecontentref_/13) --watch
```

### Running the Project

### Start the Flask server:

```sh
 python [main.py](http://_vscodecontentref_/14)
```
