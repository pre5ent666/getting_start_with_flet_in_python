import flet as ft

def main(page: ft.Page):
    t = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("First name")),
            ft.DataColumn(ft.Text("Last name")),
            ft.DataColumn(ft.Text("Age"), numeric=True),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("Smith")),
                    ft.DataCell(ft.Text("43")),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Jack")),
                    ft.DataCell(ft.Text("Brown")),
                    ft.DataCell(ft.Text("19")),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Aliceeeeeeeeeeeeeee")),
                    ft.DataCell(ft.Text("Wong")),
                    ft.DataCell(ft.Text("25")),
                ],
            ),
        ],
        expand=True,
        column_spacing=20,
        divider_thickness=0,
        vertical_lines=ft.border.BorderSide(3, "blue"),
        horizontal_lines=ft.border.BorderSide(1, "green"),
    )

    # We can use append to add new data rows into table.
    for i in [1,2,3]:
        t.rows.append(ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(f"Test_{i}")),
                        ft.DataCell(ft.Text("Cool")),
                        ft.DataCell(ft.Text(i)),
                    ],
                ),)
        
    
    page.add(t)
    

ft.app(target=main)