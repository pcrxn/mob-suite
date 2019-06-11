import mob_suite.mob_typer
import os,sys
import pandas


#test the entire mob-typer + mob_host_range modules. AB040415 has multiple replicons (IncFIB,IncFII)
def test_mob_typer_host_range_multi_replicon():
    #IncFIB,IncFII multi-plasmids
    args = [
        "--infile", os.path.dirname(__file__) + "/TestData/AB040415.fasta",
        "--outdir", "run_test",
        "--host_range_detailed"
    ]
    sys.argv[1:] = args
    mob_suite.mob_typer.main()
    results_df = pandas.read_csv("./run_test/mobtyper_AB040415_report.txt", sep="\t")

    assert results_df["NCBI-HR-rank"].values[0] == "order"
    assert results_df["NCBI-HR-Name"].values[0] == "Enterobacterales"
    assert results_df["LitRepHRPlasmClass"].values[0]  == "NarrowHostRange"
    assert results_df["LitPredDBHRRank"].values[0]  == "family"
    assert results_df["LitPredDBHRRankSciName"].values[0]  == "Enterobacteriaceae"
    assert results_df["LitRepHRRankInPubs"].values[0]  == "family"
    assert results_df["LitRepHRNameInPubs"].values[0]  == "Enterobacteriaceae"
    assert results_df["LitPMIDsNumber"].values[0]  == 5

    args = [
        "--infile", os.path.dirname(__file__) + "/TestData/AY603981.fasta",
        "--outdir", "run_test",
        "--host_range"
    ]
    sys.argv[1:] = args
    mob_suite.mob_typer.main()
    results_df = pandas.read_csv("./run_test/mobtyper_AY603981_report.txt", sep="\t")
    assert results_df["NCBI-HR-rank"].values[0] == "-"
    assert results_df["NCBI-HR-Name"].values[0] == "-"
    assert results_df["PredictedMobility"].values[0] == "Mobilizable"

    args = [
        "--infile", os.path.dirname(__file__) + "/TestData/AB011548.fasta",
        "--outdir", "run_test",
        "--host_range"
    ]
    sys.argv[1:] = args
    mob_suite.mob_typer.main()
    results_df = pandas.read_csv("./run_test/mobtyper_AY603981_report.txt", sep="\t")
    assert results_df["NCBI-HR-rank"].values[0] == "-"
    assert results_df["NCBI-HR-Name"].values[0] == "-"
    assert results_df["PredictedMobility"].values[0] == "Mobilizable"

    args = [
        "--infile", os.path.dirname(__file__) + "/TestData/AB011548.fasta",
        "--outdir", "run_test",
        "--host_range"
    ]
    sys.argv[1:] = args
    mob_suite.mob_typer.main()
    results_df = pandas.read_csv("./run_test/mobtyper_AB011548_report.txt", sep="\t")
    assert results_df["NCBI-HR-rank"].values[0] == "superkingdom"
    assert results_df["NCBI-HR-Name"].values[0] == "Bacteria"
    assert results_df["PredictedMobility"].values[0] == "Mobilizable"
    assert results_df["LitPredDBHRRank"].values[0]  == "-"
    assert results_df["LitPredDBHRRankSciName"].values[0] == "-"

def test_mob_typer_host_range_multi_replicon_KU295134():
    #KU295134.fasta with IncFII and IncN replicons
    #suitable to check the multi-replicon case and how host range data collapse is functioning
    args = [
        "--infile", os.path.dirname(__file__) + "/TestData/KU295134.fasta",
        "--outdir", "run_test",
        "--host_range_detailed"
    ]
    sys.argv[1:] = args
    mob_suite.mob_typer.main()
    results_df = pandas.read_csv("./run_test/mobtyper_KU295134_report.txt", sep="\t")


    assert results_df["NCBI-HR-rank"].values[0] == "class"
    assert results_df["NCBI-HR-Name"].values[0] == "Gammaproteobacteria"
    assert results_df["PredictedMobility"].values[0] == "Conjugative"


#check that mobtyper has literature report part non-empty


# assert any([len(re.findall("order\tEnterobacterales",out)) >= 1 for out in output]) == True, "Something went wrong with host range prediction";
# mob_typer -i /Users/kirill/WORK/MOBSuiteHostRange2018/Source/mob-suite/mob_suite/tests/TestData/IncF/ET11_Ecoli_plasmid_529.fasta -o run_test --host_range_detailed
# mob_typer -i /Users/kirill/WORK/MOBSuiteHostRange2018/Source/mob-suite/mob_suite/tests/TestData/IncF/ET5_Ecoli_plasmid_973.fasta -o run_test --host_range
# mob_typer -i /Users/kirill/WORK/MOBSuiteHostRange2018/Source/mob-suite/mob_suite/tests/TestData/IncF/ET4_Ecoli_plasmid_969.fasta -o run_test --host_range
# mob_typer -i /Users/kirill/WORK/MOBSuiteHostRange2018/Source/mob-suite/mob_suite/tests/TestData/AB040415.fasta -o run_test --host_range
# mob_typer -i /Users/kirill/WORK/MOBSuiteHostRange2018/Source/mob-suite/mob_suite/tests/TestData/AY603981.fasta -o run_test --host_range #no replicons
# mob_typer -i /Users/kirill/WORK/MOBSuiteHostRange2018/Source/mob-suite/mob_suite/tests/TestData/AB011548.fasta -o run_test --host_range_detailed
# cp  *.py /Users/kirill/miniconda/envs/mob_suite_test/lib/python3.6/site-packages/mob_suite/