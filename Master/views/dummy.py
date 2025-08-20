# app/views.py
import pandas as pd
from django.shortcuts import render, redirect
from Virtual_Showroom_db.models import ProductDetails


def upload_excel(request):
    if request.method == "POST":
        excel_file = request.FILES["file"]

        df = pd.read_excel(excel_file)

        for _, row in df.iterrows():
            ProductDetails.objects.update_or_create(
                product_code=row["Product Code"],
                defaults={
                    "style_no": row["Style No"],
                    "product_type": row["Product Type"],
                    "designer_head": row["Designer Head"],
                    "entered_by": row["Entered By"],
                    "category": row["Category"],
                    "season": row["Season"],
                    "fabric": row["Fabric"],
                    "value_driver": row["Value Driver"],
                    "sustainable": row["Sustainable"],
                    "designer_status": row["Designer Status"],
                    "dmm_status": row["DMM Status"],
                    "remarks": row["Remarks"],
                    "comment": row["Comment"],
                    "is_active": row["Is Active"],
                },
            )
        return redirect("success-page")

    return render(request, "upload.html")
