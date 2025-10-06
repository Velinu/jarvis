from langchain.tools import tool
import subprocess
import platform

@tool("open_app")
def open_app(app_name: str) -> str:
    """
    PARAMETERS
    - app_name: Application name or path to be opened

    DESCRIPTION
    - Opens an application using AppOpener or subprocess as a fallback.
    """
    try:
        if platform.system() == "Windows":
            subprocess.run(["start", "", app_name], shell=True, check=True)
        else:
            subprocess.run([app_name], check=True)
        return
    except Exception as e_appopener:
        try:
            subprocess.run([app_name], check=True)
            return
        except Exception as e_subprocess:
            return (
                f"Não foi possível abrir {app_name}.\n"
                f"Erro AppOpener: {e_appopener}\n"
                f"Erro subprocess: {e_subprocess}"
            )
