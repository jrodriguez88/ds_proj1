import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_links_data(web_url, extension):
    try:
        # Make an HTTP request to get the page content
        response = requests.get(web_url)

        # Create a BeautifulSoup object to parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all 'a' tags (links) in the HTML
        links = soup.find_all('a')

        # Extract links with the specified extension
        valid_links = [urljoin(web_url, link.get('href')) for link in links if link.get('href') and link.get('href').endswith(extension)]

        return valid_links
    
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving the page: {e}")
        return []
    

def download_documents(links, destination_directory='downloads'):
    """
    Downloads documents from a list of direct download links.

    Parameters:
        links (list): List of direct download links.
        destination_directory (str): Directory where downloaded documents will be saved.

    Returns:
        list: List of paths to the downloaded documents.
    """
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    document_paths = []

    for idx, link in enumerate(links, start=1):
        try:
            # Get the content of the document
            response = requests.get(link)
            response.raise_for_status()

            # Get the filename from the link
            file_name = os.path.join(destination_directory, f"document_{idx}.xls")

            # Save the content to a local file
            with open(file_name, 'wb') as file:
                file.write(response.content)

            document_paths.append(file_name)
            print(f"Document {idx} downloaded successfully: {file_name}")

        except requests.exceptions.RequestException as e:
            print(f"Error downloading document {idx} from {link}: {e}")

    return document_paths
