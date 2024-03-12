import arcpy
from sys import argv

def BP(Attributes_To_Join="ALL", Output_Type="INPUT", Cellsize_10_="10", Build_raster_attribute_table=True):  # BP
    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False
    # Check out any necessary licenses.
    arcpy.CheckOutExtension("3D")
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("ImageAnalyst")
    KATASTRALNI_UZEMI_P = "KATASTRALNI_UZEMI_P"
    RAD_MZCR_Ln = "RAD_MZCR_Ln"
    RAD_IPR_Ln = "RAD_IPR_Ln"
    # Process: Create Fishnet [10x10] (Create Fishnet) (management)
    RAD_Fishnet = "E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\RAD_Fishnet"
    RAD_Fishnet_label = arcpy.management.CreateFishnet(out_feature_class=RAD_Fishnet, origin_coord="-751549,69 -1055107,6", y_axis_coord="-751549,69 -1055097,6", cell_width=10, cell_height=10, number_rows=None, number_columns=None, corner_coord="-746115,65 -1050699,78", labels="LABELS", template="-751549,69 -1055107,6 -746115,65 -1050699,78 PROJCS[\"S-JTSK_Krovak_East_North\",GEOGCS[\"GCS_S_JTSK\",DATUM[\"D_S_JTSK\",SPHEROID[\"Bessel_1841\",6377397.155,299.1528128]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Krovak\"],PARAMETER[\"False_Easting\",0.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Pseudo_Standard_Parallel_1\",78.5],PARAMETER[\"Scale_Factor\",0.9999],PARAMETER[\"Azimuth\",30.28813975277778],PARAMETER[\"Longitude_Of_Center\",24.83333333333333],PARAMETER[\"Latitude_Of_Center\",49.5],PARAMETER[\"X_Scale\",-1.0],PARAMETER[\"Y_Scale\",1.0],PARAMETER[\"XY_Plane_Rotation\",90.0],UNIT[\"Meter\",1.0]]", geometry_type="POLYGON")[0]
    # Process: Clip Fishnet label (Clip) (analysis)
    RAD_Fishnet_label_Clip = "E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\RAD_Fishnet_label_Clip"
    arcpy.analysis.Clip(in_features=RAD_Fishnet_label, clip_features=KATASTRALNI_UZEMI_P, out_feature_class=RAD_Fishnet_label_Clip, cluster_tolerance="")
    # Process: Clip Fishnet (Clip) (analysis)
    RAD_Fishnet_Clip = "E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\RAD_Fishnet_Clip"
    arcpy.analysis.Clip(in_features=RAD_Fishnet, clip_features=KATASTRALNI_UZEMI_P, out_feature_class=RAD_Fishnet_Clip, cluster_tolerance="")
    # Process: Erase MZCR (Erase) (analysis)
    erase_MZCR = "E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\erase_MZCR"
    arcpy.analysis.Erase(in_features=KATASTRALNI_UZEMI_P, erase_features=RAD_MZCR_Ln, out_feature_class=erase_MZCR, cluster_tolerance="")
    # Process: Erase IPR (Erase) (analysis)
    erase_IPR = "E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\erase_IPR"
    arcpy.analysis.Erase(in_features=KATASTRALNI_UZEMI_P, erase_features=RAD_IPR_Ln, out_feature_class=erase_IPR, cluster_tolerance="")
    # Process: Merge (Merge) (management)
    erase_IPR_MZCR = "E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\erase_IPR_MZCR"
    arcpy.management.Merge(inputs=[erase_MZCR, erase_IPR], output=erase_IPR_MZCR, field_mappings="ID \"ID\" true false false 40 Text 0 0,First,#,E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\clip_MZCR,ID,0,40,E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\clip_IPR,ID,0,40;ID_2 \"ID_2\" true false false 40 Text 0 0,First,#,E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\clip_MZCR,ID_2,0,40,E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\clip_IPR,ID_2,0,40;TYPPPD_KOD \"TYPPPD_KOD\" true false false 7 Text 0 0,First,#,E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\clip_MZCR,TYPPPD_KOD,0,7,E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\clip_IPR,TYPPPD_KOD,0,7;KATUZE_KOD \"KATUZE_KOD\" true false false 6 Long 0 6,First,#,E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\clip_MZCR,KATUZE_KOD,-1,-1,E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\clip_IPR,KATUZE_KOD,-1,-1;Shape_length \"Shape_length\" true true false 0 Double 0 0,First,#,E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\clip_MZCR,Shape_length,-1,-1,E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\clip_IPR,Shape_length,-1,-1;Shape_area \"Shape_area\" true true false 0 Double 0 0,First,#,E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\clip_MZCR,Shape_area,-1,-1,E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\clip_IPR,Shape_area,-1,-1", add_source="NO_SOURCE_INFO")
    # Process: Erase MZCR_erase (Erase) (analysis)
    RAD_MZCR_correct = "E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\RAD_MZCR_Ln_Erase"
    arcpy.analysis.Erase(in_features=RAD_MZCR_Ln, erase_features=erase_IPR_MZCR, out_feature_class=RAD_MZCR_correct, cluster_tolerance="")
    # Process: Intersect (MZCR) Ln (Intersect) (analysis)
    MZCR_Ln_Fishnet = "E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\RAD_MZCR_Ln_Fishnet"
    arcpy.analysis.Intersect(in_features=[[RAD_Fishnet_Clip, ""], [RAD_MZCR_correct, ""]], out_feature_class=MZCR_Ln_Fishnet, join_attributes=Attributes_To_Join, cluster_tolerance="", output_type=Output_Type)
    # Process: Polygon to Raster (MZCR Ln) (Polygon to Raster) (conversion)
    RAD_MZCR_Ln_Raster = "E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\RAD_MZCR_Ln_Raster"
    arcpy.conversion.PolygonToRaster(in_features=MZCR_Ln_Fishnet, value_field="DB_High", out_rasterdataset=RAD_MZCR_Ln_Raster, cell_assignment="CELL_CENTER", priority_field="NONE", cellsize=Cellsize_10_, build_rat=Build_raster_attribute_table)
    # Process: Erase IPR_erase (Erase) (analysis)
    RAD_IPR_correct = "E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\RAD_IPR_Ln_Erase"
    arcpy.analysis.Erase(in_features=RAD_IPR_Ln, erase_features=erase_IPR_MZCR, out_feature_class=RAD_IPR_correct, cluster_tolerance="")
    # Process: Intersect (IPR) Ln (Intersect) (analysis)
    IPR_Ln_Fishnet = "E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\IPR_RAD_Ln_Fishnet"
    arcpy.analysis.Intersect(in_features=[[RAD_Fishnet_Clip, ""], [RAD_IPR_correct, ""]], out_feature_class=IPR_Ln_Fishnet, join_attributes=Attributes_To_Join, cluster_tolerance="", output_type=Output_Type)
    # Process: Polygon to Raster (IPR Ln) (Polygon to Raster) (conversion)
    RAD_IPR_Ln_Raster = "E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\RAD_IPR_Ln_Raster"
    arcpy.conversion.PolygonToRaster(in_features=IPR_Ln_Fishnet, value_field="DB_HI", out_rasterdataset=RAD_IPR_Ln_Raster, cell_assignment="CELL_CENTER", priority_field="NONE", cellsize=Cellsize_10_, build_rat=Build_raster_attribute_table)
    # Process: Minus (Minus) (3d)
    RAD_MZ_IPR = "E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\RAD_MZ_IPR"
    with arcpy.EnvManager(scratchWorkspace=r"D:\Skola\BP\GIS\SHM_Praha\SHM_Praha.gdb", workspace=r"D:\Skola\BP\GIS\SHM_Praha\SHM_Praha.gdb"):
        arcpy.ddd.Minus(in_raster_or_constant1=RAD_MZCR_Ln_Raster, in_raster_or_constant2=RAD_IPR_Ln_Raster, out_raster=RAD_MZ_IPR)
        RAD_MZ_IPR = arcpy.Raster(RAD_MZ_IPR)
    # Process: Raster to Point (Raster to Point) (conversion)
    RAD_Rozdil_B = "E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\RAD_Rozdil_B"
    with arcpy.EnvManager(outputMFlag="Disabled", outputZFlag="Disabled"):
        arcpy.conversion.RasterToPoint(in_raster=RAD_MZ_IPR, out_point_features=RAD_Rozdil_B, raster_field="Value")
    # Process: Raster to Polygon (Raster to Polygon) (conversion)
    RAD_Rozdil_P = "E:\\Skola\\BP\\GIS\\BP\\BP.gdb\\RAD_Rozdil_P"
    with arcpy.EnvManager(outputMFlag="Disabled", outputZFlag="Disabled"):
        arcpy.conversion.RasterToPolygon(in_raster=RAD_MZ_IPR, out_polygon_features=RAD_Rozdil_P, simplify=Build_raster_attribute_table, raster_field="Value", create_multipart_features="SINGLE_OUTER_PART", max_vertices_per_feature=None)

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"E:\Skola\BP\GIS\BP\BP.gdb", workspace=r"E:\Skola\BP\GIS\BP\BP.gdb"):
