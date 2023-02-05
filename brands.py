class Tesla:
    """
    A class to represent Tesla.
    ...

    Attributes
    ----------
    model : str
        vehicle model - must be one of ('s','3','x','y'). 
        Tesla vehicle models are listed on separate URLs, thus it's necessary to declare the model explicitly.

    Methods
    -------
    get_listing_url(zip_code='',distance_from_zip=''):
        returns vehicle listing URL to be scraped

    """
    vehicle_name_selector = 'div.result-basic-info > h3'
    vehicle_price_selector = 'div.result-pricing > div.result-price > span.result-purchase-price'
    vehicle_trim_selector = 'div.result-basic-info > div.tds-text_color--10'
    listing_root = 'https://www.tesla.com/inventory/new/m'

    def __init__(self,model='3'):
        self.model = model
        if self.model.lower() not in ('s','3','x','y'):
            raise ValueError("Model value must be one of ('s','3','x','y')")

    def get_listing_url(self,zip_code='90210',distance_from_zip=200):
        """
        Returns a string representation of the URL to be scraped for vehicle listings

        Parameters
        ----------
        zip_code : str, optional
            Zip code to search for listings. Default is '90210'
        
        distance_from_zip : int, optional
            The radius around the zip_code to search. Default is 200.

        Returns
        -------
        URL to scrape for listings
        """
        model_string = self.model.lower()
        distance_from_zip = str(distance_from_zip)
        model_listing_url = self.listing_root + model_string + '?arrangeby=relevance' + '&zip=' + zip_code + '&range=' + distance_from_zip
        return model_listing_url

    