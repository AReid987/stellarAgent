### Objectives

- Learn about the new updates in AER, including model aliases and improved context window.
- Understand how to use the qwq model as the architect and Quinn 2.5 coder as the editor model.
- Set up AER locally or use it for free with glhf API.
- Test the new features and see how to configure the models for optimal results.

### Instructions

1. **Update AER**:
   - Run the command: `pip install upgrade AER chat`

2. **Create Model Aliases**:
   - Use the Alias flag to create an alias for models with long names.
   - Example: `ader with the Alias flag`

3. **Disable URL Scraping**:
   - Use the no detect URLs flag to disable the scraping feature when pasting URLs.

4. **Set Context Window**:
   - The context window is now dynamically set to 8K for better results with Alama models.

5. **Use Inline Commands**:
   - The editor command now allows inline commands at the start of the prompt.

6. **Reference PDFs**:
   - You can now reference PDFs in the chat, and AER can read and use the context from the PDF.

7. **Select Voice Input Device**:
   - Configure the voice input device for voice recording features in AER.

8. **Configure API Call Timeouts**:
   - Use the new time option to configure API call timeouts to prevent automatic timeouts.

9. **Set Working Directory for Shell Commands**:
   - AER will automatically set the current working directory to the repo route when running shell commands.

10. **Use Keyboard Shortcuts**:
    - Use Control Plus up and down keyboard shortcuts for per message history navigation.

11. **Set Up qwq and Quinn 2.5 Coder Models**:
    - Get your API key and base URL from glhf.
    - Export environment variables for the base URL and API key or create an EnV file.
    - Create an AER config file and enable architect mode.
    - Set the default model as qwq and editor model as quen 2.5 coder.

12. **Run AER with Configured Models**:
    - Run AER to see the architect mode enabled.
    - Use the qwq model for planning and quen 2.5 coder for coding to get better results.

13. **Test the Setup**:
    - Use a basic Expo app and ask AER to make a water intake tracker app.
    - Verify that the setup works correctly and produces the desired results.

14. **Optional Local Setup**:
    - If you have a 4,090 GPU, you can run the models locally for faster speeds.
    - Use glhf for free API access if you don't want to run it locally.

15. **Provide Feedback**:
    - Share your thoughts in the comments.
    - Consider donating or becoming a member to support the channel.
    - Give the video a thumbs up and subscribe to the channel.
