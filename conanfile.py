from conans import ConanFile, tools

class AssetsDungeon(ConanFile):
    name = "assets-dungeon"
    version = "1.0"
    description = "Tileset for a dungeon"
    topics = "assets", "dungeon"
    url = "https://www.patreon.com/posts/modular-dungeon-19227322"

    exports_sources = "Dungeon Tiles.xml"

    def source(self):
        url = "https://www.patreon.com/file?h=19227322&i=2255154"
        tools.get(url, filename="tileset")

    def package_info(self):
        self.cpp_info.resdirs = ["tileset",]

    def package(self):
        self.copy("Dungeon Tiles.xml", dst="tileset")
        self.copy("*.png", dst="tileset")
        self.copy("*.jpg", dst="tileset")
