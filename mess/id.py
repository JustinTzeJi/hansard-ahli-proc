import marimo

__generated_with = "0.10.16"
app = marimo.App(width="full")


@app.cell
def _():
    import pandas as pd
    from thefuzz import fuzz, process
    import marimo as mo
    return fuzz, mo, pd, process


@app.cell
def _(pd):
    df = pd.read_csv("DR - DR 1 - 11 no ID.csv")
    return (df,)


@app.cell
def _(df):
    unique_names = df[df["vol"] == 1].nama.to_list()
    unique_names = set(unique_names)
    return (unique_names,)


@app.cell
def _(unique_names):
    name_map = {i:[i] for i in unique_names}
    return (name_map,)


@app.cell
def _(df, unique_names):
    unique_names_n = df[df["vol"] == 2].nama.to_list()
    unique_names_n = list(set(unique_names_n).difference(unique_names))
    return (unique_names_n,)


@app.cell
def _(unique_names_n):
    names = unique_names_n
    return (names,)


@app.cell
def _():
    def inc():
        if "incr" not in globals():
            global incr
            incr = 0
        else:
            incr += 1
        return incr
    return inc, incr


@app.cell
def _(mo):
    submit_b = mo.ui.button(
        label="Submit",
    )
    return (submit_b,)


@app.cell
def _(incr, mo, names, submit_b):
    mo.stop(not submit_b.value)
    current_name = names[incr if "incr" in globals() else 0]
    return (current_name,)


@app.cell
def _(current_name, mo, name_map, process):
    radio = mo.ui.radio(options=[i[0] for i in process.extract(current_name, [x for i in name_map.values() for x in i])], label=current_name, value=None)
    skip = mo.ui.button(
        value=False, on_click=lambda value: True, label = "Skip"
    )
    return radio, skip


@app.cell
def _(radio):
    radio
    return


@app.cell
def _(radio):
    radio.value
    return


@app.cell
def _(skip):
    skip
    return


@app.cell
def _(submit_b):
    submit_b
    return


@app.cell
def _(radio, skip):
    rv = radio.value
    sv = skip.value
    return rv, sv


@app.cell
def _(rv):
    rv
    return


@app.cell
def _(rv, submit_b, sv):
    if submit_b.value:

    # mo.stop(not submit_b.value)
        print("submit")
        print(rv, sv)
    # if not radio.value and not skip.value:
    #     print("a")
    #     pass
    # elif radio.value and not skip.value:
    #     if radio.value in name_map.keys():
    #         print("b")
    #         name_map[radio.value].append(current_name)
    #     else:
    #         print("c")
    #         print(f"weird: {radio.value}, {current_name}")
    # else:
    #     print("skipped")
    #     print("d")
    #     name_map[current_name] = [current_name]
    # # inc()
    return


@app.cell
def _(mo):
    mo.md("""# r_name""")
    return


@app.cell
def _(mo, name_map, radio, submit_b):
    mo.stop(not submit_b.value)
    name_map[radio.value] if radio.value else None
    return


@app.cell
def _(mo):
    mo.md("""# c_name""")
    return


@app.cell
def _(current_name, mo, name_map, submit_b):
    mo.stop(not submit_b.value)
    name_map[current_name] if current_name in name_map.keys() else None
    return


@app.cell
def _(incr, mo, submit_b):
    mo.stop(not submit_b.value)
    incr if "incr" in globals() else 0
    return


@app.cell
def _(radio):
    radio.value
    return


@app.cell
def _(skip):
    skip.value
    return


@app.cell
def _(radio):
    not radio.value
    return


@app.cell
def _(mo, submit_b, unique_names_n):
    mo.stop(not submit_b.value)
    unique_names_n[-1]
    return


@app.cell
def _(name_map):
    len(name_map)
    return


@app.cell
def _(name_map):
    name_map
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
