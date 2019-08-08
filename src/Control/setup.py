import cx_Freeze

executables = [cx_Freeze.Executable("control_view.py")]

cx_Freeze.setup(
    name="BlackJack",
    options={""}
)