
import streamlit as st
from streamlit_folium import folium_static
import folium

st.set_page_config( layout="wide",page_title="Sri!",page_icon='🎙️')
st.title("Python3 Resources Working Tools")
st.markdown("""Python’s standard library is very extensive, offering a wide range of facilities as indicated by the long table of contents listed below. The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming. Some of these modules are explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics into platform-neutral APIs.

The Python installers for the Windows platform usually include the entire standard library and often also include many additional components. For Unix-like operating systems Python is normally provided as a collection of packages, so it may be necessary to use the packaging tools provided with the operating system to obtain some or all of the optional components.

In addition to the standard library, there is an active collection of hundreds of thousands of components (from individual programs and modules to packages and entire application development frameworks), available from the [PIP](https://pypi.org/) 
""")
st.subheader("Resources in Project Hey Sri - Bot 🎙️")
st.write('''
SpeechRecognition Documentation:
SpeechRecognition Documentation: Explore the documentation to understand the capabilities and options of the SpeechRecognition library.

pyttsx3 Documentation:
pyttsx3 Documentation: Check the documentation for pyttsx3 to learn more about its features and customization options.

Web Scraping for Better Search Results:
Consider exploring web scraping techniques to extract more relevant information from search results and provide more detailed responses.

Advanced Voice Commands:
Extend the list of voice commands to cover a broader range of functionalities, such as sending emails, setting reminders, or interacting with other applications.

         
Natural Language Processing (NLP):
Integrate NLP libraries, such as spaCy or NLTK, to improve the understanding of user input and provide more natural responses.

API Integration:
Explore APIs for weather, news, or other services, and integrate them to provide real-time information.

Error Handling:
Enhance error handling to provide informative responses when the assistant doesn't understand or encounters an issue.

User Interface (UI):
Develop a simple graphical user interface (GUI) for a more user-friendly interaction.

Multi-threading:
Consider implementing multi-threading to handle simultaneous tasks and improve responsiveness.

         ''')
st.subheader("Streamlit Package 🎙️")
st.write('''
Streamlit and Emojis: Building Interactive Web Apps with Ease!

Streamlit is a fantastic Python library that empowers developers to create interactive web applications with minimal effort. 🚀 It's designed to be simple and intuitive, allowing you to turn data scripts into shareable web apps in just a few lines of code. 📊

Getting Started with Streamlit 🛠️
         
To begin, you need to install Streamlit using pip:

pip install streamlit
''')
st.subheader("Libraries or Modules 🎙️ ")
st.markdown("""

Built in modules in Python is an approach to software design that involves breaking down a program into smaller, self-contained units or modules. This has several advantages:

Facilitates Collaborative Development

By dividing the program into smaller modules, developers can work on different program parts simultaneously. This allows for faster development and testing and easier collaboration among team members.

Improves Readability and Manageability

Modular programming allows developers to organise their code into smaller, more manageable units. This makes the code easier to read, understand, and maintain. Each module can be designed, implemented, and tested independently of the others, making it easier to manage the overall program.

Enhances Reusability of Code

Modular programming makes it easier to reuse code. Modules can be designed for multiple programs, reducing the need to write new code from scratch. This saves time and effort and helps to minimize errors.

Detects Programming Errors More Easily

Since each module is self-contained, errors can be traced back to a specific module or function, making identifying and correcting them easier.

Allows for Better Program Design

Modular programming allows for better program design by breaking down complex programs into smaller, more manageable pieces. 
""")





