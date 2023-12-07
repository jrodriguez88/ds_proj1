
def get_links_data(web_url, extension):
    # Make an HTTP request to get the page content
    response = requests.get(web_url)

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')

        # Find all 'a' tags (links) in the HTML
    links = soup.find_all('a')

        # Extract links with the specified extension
    valid_links = [urljoin(web_url, link.get('href')) for link in links if link.get('href') and link.get('href').endswith(extension)]

    return valid_links
    


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


# Function to extract the month and year from each URL
def extract_month_year(url):
    # Extract the last element after "download/"
    file_name = url.split('/')[-1]

    # Extract the month and year using a regular expression
    match = re.search(r'(\w+)(\d{4})', file_name.replace('-', ''))
    if match:
        return match.group(1), match.group(2)
    else:
        return None
    

# Función completa que integra la extracción de fechas de una lista de URLs y encuentra los últimos 6 meses disponibles

def extract_dates_and_find_last_6_months(urls):
    # Diccionario para mapear nombres de meses posiblemente incompletos a nombres completos
    months = {
        'jan': 'January', 'feb': 'February', 'mar': 'March', 'apr': 'April', 
        'may': 'May', 'jun': 'June', 'jul': 'July', 'aug': 'August', 
        'sep': 'September', 'oct': 'October', 'nov': 'November', 'dec': 'December'
    }

    # Función para extraer y formatear las fechas
    def format_year_month(url):
        file_name = url.split('/')[-1].lower()
        match = re.search(r'(\w+)(\d{2,4})', file_name.replace('-', ''))
        if match:
            month_part, year = match.group(1), match.group(2)
            year = f"20{year}" if len(year) == 2 else year

            for short_month, full_month in months.items():
                if short_month in month_part:
                    return f"{year} {full_month}"

            # Intento alternativo para extraer el mes
            month_match = re.search(r'(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)', month_part)
            return f"{year} {months[month_match.group(0)]}" if month_match else None
        return None

    # Extraer y formatear las fechas de las URLs
    formatted_dates = [format_year_month(url) for url in urls]

    # Obtener la fecha actual
    current_date = datetime.now()
    current_year = current_date.year
    current_month = current_date.strftime("%B")

    # Función para obtener los últimos 6 meses disponibles
    def get_last_6_months(dates, current_year, current_month):
        valid_dates = [date for date in dates if date is not None]
        date_objects = [datetime.strptime(date, '%Y %B') for date in valid_dates]
        date_objects.sort(reverse=True)

        last_6_months = []
        for date in date_objects:
            if date.year == current_year and date.strftime("%B") == current_month:
                last_6_months.append(date)
                if len(last_6_months) == 6:
                    break
            elif date < datetime(current_year, current_date.month, 1):
                last_6_months.append(date)
                if len(last_6_months) == 6:
                    break

        return [date.strftime('%Y %B') for date in last_6_months]

    # Encontrar y devolver los últimos 6 meses disponibles
    return get_last_6_months(formatted_dates, current_year, current_month)

# Lista de URLs proporcionada
urls = [
    'https://birmingham-city-observatory.datopian.com/dataset/cf552d08-cee9-43bf-8c0f-3196a9311799/resource/b4a15ade-11b1-4c98-88a0-8cd8408212ac/download/purchasecardtransactionsapril2014.xls',
    # ... otras URLs ...
]

# Identificar los últimos 6 meses disponibles
last_6_months_available = extract_dates_and_find_last_6_months(urls)
last_6_months_available