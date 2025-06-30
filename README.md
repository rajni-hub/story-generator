# AI Story Generator

A beautiful and intuitive web application that generates creative short stories using Google's Gemini AI. Built with Streamlit, this app offers a modern, responsive interface for creating personalized stories across multiple genres.

## 📸 App Preview

![Demo Screenshot](https://github.com/rajni-hub/story-generator/blob/main/assests/pic1.png?raw=true)


## 🎥 Demo
[![Watch the video](https://drive.google.com/file/d/1E14loJ5JP-Ux3CTruh7qXSbiaoOX2L2C/view?usp=sharing)]

## Features

- **AI-Powered Story Generation**: Leverages Google Gemini 1.5 Flash for creative storytelling
- **Multiple Creativity Levels**: Choose between Creative, Balanced, or Focused writing styles
- **Genre Selection**: Generate stories in Science Fiction, Fantasy, Mystery, Romance, Horror, Adventure, or Comedy
- **Beautiful UI**: Modern, responsive design with glassmorphism effects and smooth animations
- **Sample Prompts**: Built-in inspiration with genre-specific story starters
- **Alternative Versions**: Generate multiple versions of the same story concept
- **Real-time API Testing**: Built-in API key validation and testing

## Quick Start

### Prerequisites

- Python 3.7 or higher
- A Google AI Studio API key (free)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-story-generator.git
   cd ai-story-generator
   ```

2. **Install required packages**
   ```bash
   pip install streamlit requests python-dotenv
   ```

3. **Get your Gemini API key**
   - Visit [Google AI Studio](https://aistudio.google.com)
   - Sign in with your Google account
   - Click "Get API Key" and create a new key
   - Copy the API key (starts with `AIza...`)

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open your browser**
   
   Navigate to `http://localhost:8501` to start creating stories!

## Usage

### Creating Your First Story

1. **Enter a Story Prompt**: Describe your story idea in the text area
   - Example: "A detective discovers that all the clocks in the city have stopped at the same time"

2. **Choose Settings**:
   - **Creativity Level**: 
     - *Creative*: More unexpected twists and imaginative elements
     - *Balanced*: Perfect mix of structure and creativity
     - *Focused*: More structured and coherent narrative
   
   - **Genre**: Select from 8 different genres or choose "Any" for flexibility

3. **Generate**: Click "Generate My Story" and watch the AI craft your tale

4. **Explore Alternatives**: Use "Generate Alternative Version" for different takes on the same prompt

### Sample Prompts

The app includes built-in sample prompts across different genres:

- **Sci-Fi**: "A space station receives a distress signal from Earth... but Earth was destroyed 50 years ago"
- **Fantasy**: "A librarian discovers that the books in the restricted section are actually portals to other worlds"
- **Mystery**: "Every morning, the same stranger leaves a different colored rose on your doorstep"
- **Adventure**: "You inherit a map from your grandmother, but it shows places that don't exist on Earth"

## 🛠️ Technical Details

### Architecture

```
ai-story-generator/
├── app.py              # Main Streamlit application
├── .env                # Environment variables (API key)
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

### Dependencies

- **streamlit**: Web app framework
- **requests**: HTTP requests for Gemini API
- **python-dotenv**: Environment variable management
- **os**: Operating system interface

### API Integration

The app uses Google's Gemini 1.5 Flash model via REST API:
- **Endpoint**: `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent`
- **Method**: POST
- **Authentication**: API key parameter
- **Response Format**: JSON with generated content

### Customization Options

The story generation can be customized with:

```python
creativity_settings = {
    "creative": {"temperature": 0.9, "top_p": 0.8},
    "balanced": {"temperature": 0.7, "top_p": 0.8},
    "focused": {"temperature": 0.3, "top_p": 0.8}
}
```

## API Configuration

### Gemini API Settings

- **Model**: `gemini-1.5-flash`
- **Max Output Tokens**: 300 (150-250 word stories)
- **Temperature**: 0.3-0.9 (based on creativity level)
- **Top P**: 0.8 (consistent across all levels)
- **Timeout**: 30 seconds

### Error Handling

The app handles common API errors:
- `401`: Invalid API key
- `403`: Access forbidden
- `404`: Model not found
- `429`: Rate limit exceeded
- Timeout errors
- Network connectivity issues

## 🔧 Troubleshooting

### Common Issues

**1. "API key not found in environment variables"**
- Ensure your `.env` file is in the project root
- Check that the API key is correctly formatted: `GEMINI_API_KEY=AIza...`
- Restart the Streamlit app after creating the `.env` file

**2. "Invalid API key (401)"**
- Verify your API key is correct and hasn't expired
- Make sure you copied the complete key from Google AI Studio

**3. "Rate limit exceeded (429)"**
- Wait a few minutes before trying again
- Google AI Studio has generous free tier limits, but they do exist

**4. Stories not generating**
- Check your internet connection
- Try a simpler prompt first
- Verify the API key is working with the built-in test feature

### Performance Tips

- Keep prompts concise but descriptive (1-2 sentences work best)
- Use the "Focused" creativity setting for more consistent results
- Try different genre combinations for unique stories

## Customization

### Styling

The app uses extensive CSS customization with:
- Custom fonts (Inter, Poppins)
- Glassmorphism effects
- Smooth animations and transitions
- Responsive design for mobile devices
- Custom color scheme with gradients

### Adding New Features

Easy extension points:
- Add new genres in the `genre_hint` selectbox
- Modify creativity settings in `creativity_settings`
- Add new sample prompts in the `sample_prompts` dictionary
- Customize the story length by changing `maxOutputTokens`

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Ideas for Contributions

- Additional story genres
- Story length options (flash fiction, longer stories)
- Export stories to different formats
- Story rating and favorites system
- Multiple language support
- Character and plot development tools

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/rajni-hub/story-generator/issues) page
2. Create a new issue with:
   - Description of the problem
   - Steps to reproduce
   - Your operating system and Python version
   - Error messages (if any)

## Acknowledgments

- **Google AI Studio** for providing the Gemini API
- **Streamlit** for the amazing web app framework
- **The open-source community** for inspiration and support

---

**Made with ❤️ by [Rajni]**

*Create unlimited stories with the power of AI and your imagination!*
