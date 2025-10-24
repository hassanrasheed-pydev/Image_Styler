🖼️ Image Styler with KNN

A simple yet powerful image stylization web app built with FastAPI and K-Nearest Neighbors (KNN) for color quantization.
Upload any image — and watch it transform into multiple artistic versions with reduced color palettes, offering a “stylized” look.

🚀 Features

Lightweight & Fast — powered by FastAPI and optimized KNN clustering.

Smart Styling — generates multiple stylized versions automatically (2–12 color groups).

Interactive Slider — preview all styles smoothly without clutter.

Modern Dark UI — elegant, user-friendly interface refined using Claude 4.5 Sonnet for UI enhancement.

Fully Modular — core logic isolated in styler.py, server handled by server.py.

🧠 Tech Stack

Backend: FastAPI

Frontend: HTML5, TailwindCSS (custom dark theme)

Model: KNN-based color quantization

Additional Tools: Pillow, NumPy, Scikit-learn

📂 Project Structure
ImageStyler/
|
├── outputs/
│   └── styles_2.jpeg, ....
├── styler.py         # Contains KNN-based image stylization pipeline
├── server.py         # FastAPI app
├── test.py           # For Testing (optional)
├── templates/
│   └── index.html    # Dark-themed frontend
└── README.md
└──other neccecry files too # like(uv.lock, pyproject.toml, etc)

⚙️ Usage
1. Install Dependencies
pip install fastapi uvicorn pillow scikit-learn numpy

2. Run Server
uvicorn server:app --reload

3. Open in Browser

Visit 👉 Comming Sooooooon!

Upload an image and slide through different stylized versions.

💡 Credits

Core logic, ML pipeline, and design structure — developed by me.

UI refinement and visual enhancements — inspired and optimized with help from Claude 4.5 Sonnet.

🧾 License

MIT License — free to use, modify, and distribute
