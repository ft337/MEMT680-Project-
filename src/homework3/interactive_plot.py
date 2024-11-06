import os 
import random
from PIL import Image
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import base64

# Initialize the Dash app for more documentation on Dash: https://dash.plotly.com/
app = dash.Dash(__name__)

# Path to dataset 
dataset_path = '/Users/fatimatariq/Desktop/Homework3_MEMT680/SLiBR_dataset/classification' 

# These are the folders within the dataset 
categories = ["anode", "cathode", "nothing"]

# Helper function to encode images for display in Dash

def encode_image(image_path):
    """ 
    Encodes an image file in base64 format for display in HTML.  

    Args:
        image_path (str): The path to image file. 

    Returns:
        str: A base64-encoded string representing the image in HTML format. 
    """
    with open(image_path, 'rb') as image_file:
        encoded = base64.b64encode(image_file.read()).decode('ascii')   # Reads an image file in binary mode and encodes it to base64 (format suitable for embedding in HTML)
    return f"data:image/jpeg;base64,{encoded}"                          #tells HTML to interpret the string as an inline JPEG image 

# Layout of the Dash app, defining the structure and layout of the app 
app.layout = html.Div(
    style={
        'backgroundColor': '#1a1a1a',           # Set background color of app 
        'color': 'white',                       # Set defaul text color 
        'padding': '20px',                      # Add padding around entire layout 
        'fontFamily': 'Arial, sans-serif',      # Set font family 
        'textAlign': 'center'                   # Center-align text in the layout 
    },
    children=[
        # App title 
        html.H1(
            "Interactive SLiBR Image Viewer",
            style={'fontSize': '36px', 
                   'fontWeight': 'bold', 
                   'marginBottom': '30px'}
        ),
        
        # Dropdown for selecting a category
        # This is the main container styled with backgroundColor, color (text), padding (space around content), fontFamily, textAlign
        html.Div([
            html.Label("Select a Category:", style={'fontSize': '20px', 'marginBottom': '10px'}),
            dcc.Dropdown(
                id='category-dropdown',
                options=[{'label': cat.capitalize(), 'value': cat} for cat in categories],
                value='anode',                  # Default value for dropwdown 
                style={'width': '50%', 
                       'margin': '0 auto', 
                       'color': '#333'}
            ),
        ], style={'marginBottom': '30px'}),

        # Slider for selecting the number of images to display
        html.Div([
            html.Label("Number of Images to Display:", style={'fontSize': '20px', 'marginBottom': '10px'}),
            dcc.Slider(
                id='num-images-slider',
                min=1,
                max=10,
                step=1,
                value=5,                         # Default number of images 
                marks={i: str(i) for i in range(1, 11)},
                tooltip={"placement": "bottom", "always_visible": True},
            ),
        ], style={'width': '60%', 'margin': '0 auto', 'marginBottom': '30px'}),
        
        # Container for displaying images
        html.Div(
            id='image-gallery',
            style={
                'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'center', 
                'gap': '20px', 'marginTop': '20px'
            }
        ),
    ]
)

# Callback to update images based on user input
@app.callback(
    Output('image-gallery', 'children'),
    [Input('category-dropdown', 'value'),
     Input('num-images-slider', 'value')]
)

def update_images(category, num_images):
    """
    Updates the displayed images in the gallery based on the selected category and 
    number of images. 

    Args:
        category (str): The selected image category (e.g., "anode", "cathode", "nothing"). 
        num_images (int): The number of images to display. 

    Returns:
        list: A list of HTML image elements to be displayed in the gallery. 
        If the categroy path does not exist, it returns a message wrapped in an HTML Div element. 
    """
    category_path = os.path.join(dataset_path, category)
    if not os.path.exists(category_path):
        return [html.Div("No images available in this category.", style={'color': 'red'})]
    
    # Get list of images in the selected category
    image_files = [f for f in os.listdir(category_path) if f.endswith('.jpg')]
    selected_images = random.sample(image_files, min(num_images, len(image_files)))
    
    # Display selected images
    images = []
    for img_file in selected_images:
        img_path = os.path.join(category_path, img_file)
        encoded_img = encode_image(img_path)
        images.append(html.Img(
            src=encoded_img,
            style={
                'height': '200px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.3)',
                'border': '2px solid #ffffff', 'padding': '5px'
            }
        ))
    return images
def main():
    app.run_server(debug=True)

# Run the Dash app
if __name__ == '__main__':
    main()

