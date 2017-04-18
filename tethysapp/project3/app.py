from tethys_sdk.base import TethysAppBase, url_map_maker


class Project3(TethysAppBase):
    """
    Tethys app class for Project3.
    """

    name = 'Hydro Power'
    index = 'project3:home'
    icon = 'project3/images/icon.gif'
    package = 'project3'
    root_url = 'project3'
    color = '#f1c40f'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='project3',
                           controller='project3.controllers.home'),
        )

        return url_maps