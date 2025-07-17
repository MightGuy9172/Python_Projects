# Blog Templating Project

A simple blog web application built with Flask, demonstrating dynamic content rendering using Jinja2 templates and fetching posts from an external API.

## Features

- Home page listing all blog posts with title and subtitle.
- Individual post pages displaying full content.
- Responsive and modern UI using custom CSS and Google Fonts.
- Posts are loaded dynamically from a public JSON API.

- **main.py**: Flask application entry point, routes, and logic.
- **post.py**: Defines the `Post` class for blog post objects.
- **static/css/styles.css**: Custom styles for the blog.
- **templates/index.html**: Home page template listing all posts.
- **templates/post.html**: Template for individual post details.

## Getting Started

### Prerequisites

- Python 3.x
- Flask (`pip install flask`)
- Requests (`pip install requests`)

### Installation

1. Clone or download this repository.
2. Install dependencies:
   ```sh
   pip install flask requests
   ```

### Running the Application

1. Start the Flask server:
   ```sh
   python main.py
   ```
2. Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## How It Works

- On startup, `main.py` fetches blog post data from [npoint.io](https://api.npoint.io/c790b4d5cab58020d391).
- Each post is converted into a [`Post`](post.py) object.
- The home route (`/`) renders [`index.html`](templates/index.html) with all posts.
- Clicking "Read" on a post navigates to `/post/<id>`, rendering [`post.html`](templates/post.html) for that post.

## Customization

- To change the style, edit [`static/css/styles.css`](static/css/styles.css).
- To modify templates, edit [`templates/index.html`](templates/index.html) and [`templates/post.html`](templates/post.html).
- You can point to a different API or add your own posts by modifying the API URL in [`main.py`](main.py).

## License

This project is for educational purposes.

## Credits

- Made with ♥️
