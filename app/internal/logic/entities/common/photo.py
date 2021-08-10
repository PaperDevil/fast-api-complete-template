from app.conf.server import FULL_FILES_LINK
from app.internal.logic.entities.common.file import File
from app.internal.logic.entities.response.photo import PhotoResponse


class Photo(File):
    def to_photo_simple_response(self) -> PhotoResponse:
        return PhotoResponse(
            short_link=self.short_url,
            full_link=self.get_full_url()
        )

    def create_full_url(self):
        path = self.short_url.split('/')
        filename = path[len(path) - 1]
        self.full_url = FULL_FILES_LINK + '/' + filename

    def get_full_url(self):
        self.create_full_url()
        return self.full_url

    def __repr__(self):
        return f'Photo(full_url={self.full_url}, short_url={self.short_url})'
