from .GrabSH import grab_from_sh_replied
from .GrabSH import grab_from_sh_unreplied
from .GrabSH import set_max_page_number
from .GrabSZ import grab_from_sz_replied
from .GrabSZ import grab_from_sz_all


__all__ = ("grab_from_sh_unreplied", "grab_from_sh_replied", "grab_from_sz_replied", "grab_from_sz_all", "set_max_page_number")

if __name__ == "__main__":
    print("Module to grab Q&A data from Shanghai and Shenzhen stock exchange investor relations database.")