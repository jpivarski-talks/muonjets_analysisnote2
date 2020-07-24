import ROOT, array
execfile("/home/pivarski/bin/root/tdrstyle.py")
c1 = ROOT.TCanvas()

from math import *
import glob

DataSep17 = map(ROOT.TFile, glob.glob("/NOBACKUP/results/MuonJetsAnalysis/FitNtuple/FitNtuple_DataSep17_CMSSW382_v6_*.root"))
Data2010B = map(ROOT.TFile, glob.glob("/NOBACKUP/results/MuonJetsAnalysis/FitNtuple/FitNtuple_Data2010BPromptAll_CMSSW384_v6_*.root"))

inclBB2mu = map(ROOT.TFile, glob.glob("/NOBACKUP/results/MuonJetsAnalysis/FitNtuple/FitNtuple_inclBB2mu_CMSSW384_v6_*.root"))
inclBB4mu = map(ROOT.TFile, glob.glob("/NOBACKUP/results/MuonJetsAnalysis/FitNtuple/FitNtuple_inclBB4mu_CMSSW384_v6_*.root"))
InclusiveMuPt30 = map(ROOT.TFile, glob.glob("/NOBACKUP/results/MuonJetsAnalysis/FitNtuple/FitNtuple_InclusiveMu5_Pt30_CMSSW382_v6_*.root"))
InclusiveMuPt50 = map(ROOT.TFile, glob.glob("/NOBACKUP/results/MuonJetsAnalysis/FitNtuple/FitNtuple_InclusiveMu5_Pt50_CMSSW382_v6_*.root"))
InclusiveMuPt150 = map(ROOT.TFile, glob.glob("/NOBACKUP/results/MuonJetsAnalysis/FitNtuple/FitNtuple_InclusiveMu5_Pt150_CMSSW382_v6_*.root"))
InclusiveMuPt250 = map(ROOT.TFile, glob.glob("/NOBACKUP/results/MuonJetsAnalysis/FitNtuple/FitNtuple_InclusiveMu5_Pt250_CMSSW382_v6_*.root"))
InclusiveMuPt350 = map(ROOT.TFile, glob.glob("/NOBACKUP/results/MuonJetsAnalysis/FitNtuple/FitNtuple_InclusiveMu5_Pt350_CMSSW382_v6_*.root"))
DrellYan = map(ROOT.TFile, glob.glob("/NOBACKUP/results/MuonJetsAnalysis/FitNtuple/FitNtuple_DrellYanPythia8_CMSSW382_v6_*.root"))

JPsi = map(ROOT.TFile, glob.glob("/NOBACKUP/results/MuonJetsAnalysis/FitNtuple/FitNtuple_JPsiToMuMu_CMSSW382_v6_*.root"))
Psi2SJPsi = map(ROOT.TFile, glob.glob("/NOBACKUP/results/MuonJetsAnalysis/FitNtuple/FitNtuple_Psi2SToJpsiPiPi_CMSSW382_v6_*.root"))
Psi2S = map(ROOT.TFile, glob.glob("/NOBACKUP/results/MuonJetsAnalysis/FitNtuple/FitNtuple_Psi2SToMuMu_CMSSW382_v6_*.root"))

PairGun = map(ROOT.TFile, glob.glob("/NOBACKUP/results/MuonJetsAnalysis/FitNtuple/FitNtuple_PairGun100_alternating_CMSSW382_v6_*.root"))

########################################################
# MC extremes

# tdrStyle.SetPadLeftMargin(0.2)
# tdrStyle.SetPadRightMargin(0.05)
# c1.ResetAttPad()
# c1.Size(1., 1.)

# mass_decays_in_flight = ROOT.TH1F("mass_decays_in_flight", "", 19, 0.25, 5.)
# for tfile in InclusiveMuPt30:
#     tfile.Get("FitNtuple/lowdimuon").Draw("mass >> +mass_decays_in_flight", "containstrig > 0.5 && trigger > 1.5 && (genLevel == 4 || genLevel == 5 || genLevel == 6 || genLevel == 7 || genLevel == 12 || genLevel == 13 || genLevel == 14 || genLevel == 15)")
# mass_decays_in_flight.SetXTitle("mass [GeV/c^{2}]"); mass_decays_in_flight.GetXaxis().CenterTitle()
# mass_decays_in_flight.SetYTitle("arbitrary units"); mass_decays_in_flight.GetYaxis().CenterTitle(); mass_decays_in_flight.GetYaxis().SetTitleOffset(1.5)
# mass_decays_in_flight.Scale(1./mass_decays_in_flight.GetEntries())

# mass_missing_mcmatch = ROOT.TH1F("mass_missing_mcmatch", "", 19, 0.25, 5.)
# for tfile in InclusiveMuPt30:
#     tfile.Get("FitNtuple/lowdimuon").Draw("mass >> +mass_missing_mcmatch", "containstrig > 0.5 && trigger > 1.5 && (genLevel == 8 || genLevel == 9 || genLevel == 10 || genLevel == 11 || genLevel == 12 || genLevel == 13 || genLevel == 14 || genLevel == 15)")
# mass_missing_mcmatch.SetXTitle("mass [GeV/c^{2}]"); mass_missing_mcmatch.GetXaxis().CenterTitle()
# mass_missing_mcmatch.SetYTitle("arbitrary units"); mass_missing_mcmatch.GetYaxis().CenterTitle(); mass_missing_mcmatch.GetYaxis().SetTitleOffset(1.5)
# mass_missing_mcmatch.Scale(1./mass_missing_mcmatch.GetEntries())

# mass_drellyan = ROOT.TH1F("mass_drellyan", "", 95, 0.25, 5.)
# for tfile in DrellYan:
#     tfile.Get("FitNtuple/lowdimuon").Draw("mass >> +mass_drellyan", "containstrig > 0.5 && trigger > 1.5")
# mass_drellyan.SetXTitle("mass [GeV/c^{2}]"); mass_drellyan.GetXaxis().CenterTitle()
# mass_drellyan.SetYTitle("arbitrary units"); mass_drellyan.GetYaxis().CenterTitle(); mass_drellyan.GetYaxis().SetTitleOffset(1.5)
# mass_drellyan.Scale(1./mass_drellyan.GetEntries())

# mass_bjets = ROOT.TH1F("mass_bjets", "", 95, 0.25, 5.)
# for tfile in InclusiveMuPt30:
#     tfile.Get("FitNtuple/lowdimuon").Draw("mass >> +mass_bjets", "containstrig > 0.5 && trigger > 1.5 && (genLevel % 2 == 1)")
# mass_bjets2 = ROOT.TH1F("mass_bjets2", "", 95, 0.25, 5.)
# for tfile in inclBB2mu:
#     tfile.Get("FitNtuple/lowdimuon").Draw("mass >> +mass_bjets2", "containstrig > 0.5 && trigger > 1.5")
# mass_bjets.Scale(1./mass_bjets.Integral(1, 40))
# mass_bjets2.Scale(1./mass_bjets2.Integral(1, 40))

# mass_decays_in_flight.SetAxisRange(0., 0.25, "Y")
# mass_decays_in_flight.SetLineColor(ROOT.kGreen+2); mass_decays_in_flight.SetLineWidth(3)
# mass_missing_mcmatch.SetLineStyle(2); mass_missing_mcmatch.SetLineWidth(3)
# mass_decays_in_flight.Draw()
# mass_missing_mcmatch.Draw("same")
# tlegend = ROOT.TLegend(0.55, 0.7, 0.85, 0.9, "inclusive-#mu MC")
# tlegend.SetBorderSize(0); tlegend.SetFillColor(ROOT.kWhite); tlegend.SetTextSize(0.03)
# tlegend.AddEntry(mass_decays_in_flight, "decays in flight", "l")
# tlegend.AddEntry(mass_missing_mcmatch, "unmatched muon", "l")
# tlegend.Draw()
# c1.SaveAs("FINALPLOTS/mc_mass_spectra_fakes.pdf")

# mass_drellyan.SetLineColor(ROOT.kOrange+3); mass_drellyan.SetLineWidth(3)
# mass_drellyan.Draw()
# tlegend = ROOT.TLegend(0.45, 0.7, 0.85, 0.9)
# tlegend.SetBorderSize(0); tlegend.SetFillColor(ROOT.kWhite); tlegend.SetTextSize(0.03)
# tlegend.AddEntry(mass_drellyan, "Drell-Yan MC (Pythia 8)", "l")
# tlegend.Draw()
# c1.SaveAs("FINALPLOTS/mc_mass_spectra_drellyan.pdf")

# mass_bjets.SetAxisRange(0., 0.08, "Y")
# mass_bjets.SetXTitle("mass [GeV/c^{2}]"); mass_bjets.GetXaxis().CenterTitle()
# mass_bjets.SetYTitle("arbitrary units"); mass_bjets.GetYaxis().CenterTitle(); mass_bjets.GetYaxis().SetTitleOffset(1.5)
# mass_bjets.SetLineColor(ROOT.kRed+1); mass_bjets.SetLineWidth(3)
# mass_bjets2.SetLineColor(ROOT.kBlue); mass_bjets2.SetLineStyle(2); mass_bjets2.SetLineWidth(3)
# mass_bjets.Draw()
# mass_bjets2.Draw("same")
# tlegend = ROOT.TLegend(0.25, 0.7, 0.6, 0.9, "b#bar{b} MC (#hat{p}_{T} > 30 GeV/c)")
# tlegend.SetBorderSize(0); tlegend.SetFillColor(ROOT.kWhite); tlegend.SetTextSize(0.03)
# tlegend.AddEntry(mass_bjets, "Pythia 6", "l")
# tlegend.AddEntry(mass_bjets2, "Pythia 6 + EvtGen", "l")
# tlegend.Draw()
# c1.SaveAs("FINALPLOTS/mc_mass_spectra_bbbar.pdf")

########################################################
# background-enriched samples

tdrStyle.SetPadRightMargin(0.15)
tdrStyle.SetStatFontSize(0.05)
tdrStyle.SetStatW(0.15)
tdrStyle.SetStatX(0.9)
tdrStyle.SetStatY(0.97)
tdrStyle.SetOptFit(11)
tdrStyle.SetStatTextColor(ROOT.kRed)
c1.ResetAttPad()
c1.Size(1.5, 1.)

background_ansatz1 = ROOT.TF1("background_ansatz1", "[0]*([1]*exp(-(x-0.78265)**2 / 2. / 0.011**2) + [2]*exp(-(x-1.019455)**2 / 2. / 0.014**2) + exp(-(x-3.096916)**2 / 2. / 0.025**2) + [3]*exp(-(x-3.68609)**2 / 2. / 0.029**2) + [4]/x) + [5]/x + [6] + [7]*(x-5.) + [8]*(x-5.)**2 + [9]*(x-5.)**3 + [10]*(x-5.)**4", 0.25, 5.)
background_ansatz1.SetParNames("p_{R}", "f_{#omega}", "f_{#phi}", "f_{#psi}", "f_{m}", "p_{-1}", "p_{0}", "p_{1}", "p_{2}", "p_{3}", "p_{4}")
background_ansatz1.FixParameter(5, 0.)
background_ansatz1.SetNpx(800)

hmass = ROOT.TH1F("hmass", "", 190, 0.25, 5.); hmass.SetXTitle("mass [GeV/c^{2}]"); hmass.GetXaxis().CenterTitle()
hmass.SetYTitle("events per 0.025 GeV/c^{2}"); hmass.GetYaxis().CenterTitle()
hmass_mc = ROOT.TH1F("hmass_mc", "", 190, 0.25, 5.); hmass_mc.SetLineColor(ROOT.kBlue); hmass_mc.SetLineStyle(2)
hmass.SetLineWidth(2); hmass_mc.SetLineWidth(3)
for tfile in DataSep17 + Data2010B:
    tfile.Get("FitNtuple/lowdimuon").Draw("mass >> +hmass", "containstrig > 0.5 && trigger > 1.5 && (iso > 4.5 || ((pluspx+minuspx)*vx + (pluspy+minuspy)*vy)/sqrt((pluspx+minuspx)**2 + (pluspy+minuspy)**2) > 0.2)")
for tfile in inclBB4mu:
    tfile.Get("FitNtuple/dimudimu").Draw("massC >> +hmass_mc", "containstrig > 0.5 && trigger > 1.5")
hmass_mc.Scale(hmass.GetEntries() / hmass_mc.GetEntries())
hmass.Fit("background_ansatz1", "LR")
hmass.Fit("background_ansatz1", "LR")
hmass.GetFunction("background_ansatz1").SetLineWidth(3)
hmass.SetAxisRange(0., 280., "Y")
hmass.Draw("e1")
hmass_mc.Draw("same")
tlegend = ROOT.TLegend(0.16, 0.75, 0.5, 0.9)
tlegend.SetBorderSize(0); tlegend.SetFillColor(ROOT.kWhite); tlegend.SetTextSize(0.03)
tlegend.AddEntry(hmass, "data: dimuon with b#bar{b} cuts", "p")
tlegend.AddEntry(hmass.GetFunction("background_ansatz1"), "fit to data", "l")
tlegend.AddEntry(hmass_mc, "MC (corresponding signal region)", "l")
tlegend.Draw()
c1.SaveAs("FINALPLOTS/backgroundEnriched_massC.pdf")

prediction = 0.002 * (hmass.Integral(110, 118)/hmass.Integral()) * ((hmass.Integral(1, 109) + hmass.Integral(119, 190))/hmass.Integral()) * hmass.GetEntries()
background_dimudimuC = background_ansatz1.Clone()
background_dimudimuC.SetParameters(*[(prediction/hmass.GetEntries() if i in (0, 5, 6, 7, 8, 9, 10) else 1.)*hmass.GetFunction("background_ansatz1").GetParameter(i) for i in range(11)])
background_dimudimuC_50 = background_ansatz1.Clone(); background_dimudimuC_50.SetLineStyle(2)
background_dimudimuC_50.SetParameters(*[(50.*prediction/hmass.GetEntries() if i in (0, 5, 6, 7, 8, 9, 10) else 1.)*hmass.GetFunction("background_ansatz1").GetParameter(i) for i in range(11)])
resonance_parameters = {1: hmass.GetFunction("background_ansatz1").GetParameter(1),
                        2: hmass.GetFunction("background_ansatz1").GetParameter(2),
                        3: hmass.GetFunction("background_ansatz1").GetParameter(3),
                        4: hmass.GetFunction("background_ansatz1").GetParameter(4),
                        }

background_ansatz2 = ROOT.TF1("background_ansatz2", "[0]*([1]*exp(-(x-0.78265)**2 / 2. / 0.011**2) + [2]*exp(-(x-1.019455)**2 / 2. / 0.014**2) + exp(-(x-3.096916)**2 / 2. / 0.025**2) + [3]*exp(-(x-3.68609)**2 / 2. / 0.029**2) + [4]/x) + [5]/x + [6] + [7]*(x-5.) + [8]*(x-5.)**2 + [9]*(x-5.)**3 + [10]*(x-5.)**4", 0.25, 5.)
background_ansatz2.SetParNames("p_{R}", "f_{#omega}", "f_{#phi}", "f_{#psi}", "f_{m}", "p_{-1}", "p_{0}", "p_{1}", "p_{2}", "p_{3}", "p_{4}")
background_ansatz2.FixParameter(1, resonance_parameters[1])
background_ansatz2.FixParameter(2, resonance_parameters[2])
background_ansatz2.FixParameter(3, resonance_parameters[3])
background_ansatz2.FixParameter(4, resonance_parameters[4])
background_ansatz2.FixParameter(5, 0.)
background_ansatz2.SetNpx(800)

hmass = ROOT.TH1F("hmass", "", 190, 0.25, 5.); hmass.SetXTitle("mass [GeV/c^{2}]"); hmass.GetXaxis().CenterTitle()
hmass.SetYTitle("events per 0.025 GeV/c^{2}"); hmass.GetYaxis().CenterTitle()
hmass_mc = ROOT.TH1F("hmass_mc", "", 190, 0.25, 5.); hmass_mc.SetLineColor(ROOT.kBlue); hmass_mc.SetLineStyle(2)
hmass.SetLineWidth(2); hmass_mc.SetLineWidth(3)
for tfile in DataSep17 + Data2010B:
    tfile.Get("FitNtuple/dimuorphan").Draw("mass >> +hmass", "orphanpt > 15. && abs(orphaneta) < 0.9 && containstrig > 0.5 && trigger > 1.5")
for tfile in inclBB4mu:
    tfile.Get("FitNtuple/dimudimu").Draw("massF >> +hmass_mc", "containstrig > 0.5 && trigger > 1.5")
hmass_mc.Scale(hmass.GetEntries() / hmass_mc.GetEntries())
hmass.Fit("background_ansatz2", "LR")
hmass.Fit("background_ansatz2", "LR")
hmass.GetFunction("background_ansatz2").SetLineWidth(3)
hmass.SetAxisRange(0., 14., "Y")
hmass.Draw("e1")
hmass_mc.Draw("same")
tlegend = ROOT.TLegend(0.16, 0.75, 0.5, 0.9)
tlegend.SetBorderSize(0); tlegend.SetFillColor(ROOT.kWhite); tlegend.SetTextSize(0.03)
tlegend.AddEntry(hmass, "data: dimuon + third muon", "p")
tlegend.AddEntry(hmass.GetFunction("background_ansatz2"), "fit to data", "l")
tlegend.AddEntry(hmass_mc, "MC (corresponding signal region)", "l")
tlegend.Draw()
c1.SaveAs("FINALPLOTS/backgroundEnriched_massF.pdf")

background_dimudimuF = background_ansatz2.Clone()
background_dimudimuF.SetParameters(*[(prediction/hmass.GetEntries() if i in (0, 5, 6, 7, 8, 9, 10) else 1.)*hmass.GetFunction("background_ansatz2").GetParameter(i) for i in range(11)])
background_dimudimuF_50 = background_ansatz2.Clone(); background_dimudimuF_50.SetLineStyle(2)
background_dimudimuF_50.SetParameters(*[(50.*prediction/hmass.GetEntries() if i in (0, 5, 6, 7, 8, 9, 10) else 1.)*hmass.GetFunction("background_ansatz2").GetParameter(i) for i in range(11)])

background_ansatz3 = ROOT.TF1("background_ansatz3", "[0]*([1]*exp(-(x-0.78265)**2 / 2. / 0.011**2) + [2]*exp(-(x-1.019455)**2 / 2. / 0.014**2) + exp(-(x-3.096916)**2 / 2. / 0.025**2) + [3]*exp(-(x-3.68609)**2 / 2. / 0.029**2) + [4]/x) + [5]/x + [6] + [7]*(x-5.) + [8]*(x-5.)**2 + [9]*(x-5.)**3 + [10]*(x-5.)**4", 0.25, 5.)
background_ansatz3.SetParNames("p_{R}", "f_{#omega}", "f_{#phi}", "f_{#psi}", "f_{m}", "p_{-1}", "p_{0}", "p_{1}", "p_{2}", "p_{3}", "p_{4}")
background_ansatz3.FixParameter(5, 0.)
background_ansatz3.SetNpx(800)

hmass = ROOT.TH1F("hmass", "", 190, 0.25, 5.); hmass.SetXTitle("mass [GeV/c^{2}]"); hmass.GetXaxis().CenterTitle()
hmass.SetYTitle("events per 0.025 GeV/c^{2}"); hmass.GetYaxis().CenterTitle()
hmass.SetLineWidth(2)
hmass2 = ROOT.TH1F("hmass2", "", 190, 0.25, 5.)
for tfile in DataSep17 + Data2010B:
    tfile.Get("FitNtuple/lowdimuon").Draw("mass >> +hmass", "containstrig > 0.5 && trigger > 1.5 && 40. < pt && pt < 60.")
    tfile.Get("FitNtuple/lowdimuon").Draw("mass >> +hmass2", "containstrig > 0.5 && trigger > 1.5 && 60. < pt && pt < 80.")
hmass.Fit("background_ansatz3", "LR")
hmass.Fit("background_ansatz3", "LR")
hmass.GetFunction("background_ansatz3").SetLineWidth(3)
hmass.SetAxisRange(0., 45., "Y")
hmass.Draw("e1")
scale4060_6080 = hmass2.GetEntries() / hmass.GetEntries()
background_highdimuon = background_ansatz3.Clone()
background_highdimuon.SetParameters(*[(scale4060_6080 if i in (0, 5, 6, 7, 8, 9, 10) else 1.)*hmass.GetFunction("background_ansatz3").GetParameter(i) for i in range(11)])
tlegend = ROOT.TLegend(0.17, 0.8, 0.5, 0.9)
tlegend.SetBorderSize(0); tlegend.SetFillColor(ROOT.kWhite); tlegend.SetTextSize(0.03)
tlegend.AddEntry(hmass, "data: dimuon 40 < p_{T} < 60 GeV/c", "p")
tlegend.AddEntry(hmass.GetFunction("background_ansatz3"), "fit to data", "l")
tlegend.Draw()
c1.SaveAs("FINALPLOTS/backgroundEnriched_highpt.pdf")

resonance_parameters = {1: hmass.GetFunction("background_ansatz3").GetParameter(1),
                        2: hmass.GetFunction("background_ansatz3").GetParameter(2),
                        3: hmass.GetFunction("background_ansatz3").GetParameter(3),
                        4: hmass.GetFunction("background_ansatz3").GetParameter(4),
                        }

background_ansatz4 = ROOT.TF1("background_ansatz4", "[0]*([1]*exp(-(x-0.78265)**2 / 2. / 0.011**2) + [2]*exp(-(x-1.019455)**2 / 2. / 0.014**2) + exp(-(x-3.096916)**2 / 2. / 0.025**2) + [3]*exp(-(x-3.68609)**2 / 2. / 0.029**2) + [4]/x) + [5]/x + [6] + [7]*(x-5.) + [8]*(x-5.)**2 + [9]*(x-5.)**3 + [10]*(x-5.)**4", 0.25, 5.)
background_ansatz4.SetParNames("p_{R}", "f_{#omega}", "f_{#phi}", "f_{#psi}", "f_{m}", "p_{-1}", "p_{0}", "p_{1}", "p_{2}", "p_{3}", "p_{4}")
background_ansatz4.FixParameter(1, resonance_parameters[1])
background_ansatz4.FixParameter(2, resonance_parameters[2])
background_ansatz4.FixParameter(3, resonance_parameters[3])
background_ansatz4.FixParameter(4, resonance_parameters[4])
background_ansatz4.SetNpx(800)

hmass = ROOT.TH1F("hmass", "", 190, 0.25, 5.); hmass.SetXTitle("mass [GeV/c^{2}]"); hmass.GetXaxis().CenterTitle()
hmass.SetYTitle("events per 0.025 GeV/c^{2}"); hmass.GetYaxis().CenterTitle()
hmass_mc = ROOT.TH1F("hmass_mc", "", 190, 0.25, 5.); hmass_mc.SetLineColor(ROOT.kBlue); hmass_mc.SetLineStyle(2)
hmass.SetLineWidth(2); hmass_mc.SetLineWidth(3)
hmass2 = ROOT.TH1F("hmass2", "", 190, 0.25, 5.)
for tfile in DataSep17 + Data2010B:
    tfile.Get("FitNtuple/mujetplustracks").Draw("massa >> +hmass", "containstrig > 0.5 && trigger > 1.5 && muons == 2 && fakes == 2 && charge == 0")
    tfile.Get("FitNtuple/mujetplustracks").Draw("massb >> +hmass", "containstrig > 0.5 && trigger > 1.5 && muons == 2 && fakes == 2 && charge == 0")
    tfile.Get("FitNtuple/mujetplustracks").Draw("massa >> +hmass2", "containstrig > 0.5 && trigger > 1.5 && muons == 3 && fakes == 1 && charge == 0")
    tfile.Get("FitNtuple/mujetplustracks").Draw("massb >> +hmass2", "containstrig > 0.5 && trigger > 1.5 && muons == 3 && fakes == 1 && charge == 0")
for tfile in InclusiveMuPt30 + InclusiveMuPt50 + InclusiveMuPt150 + InclusiveMuPt250 + InclusiveMuPt350:
    tfile.Get("FitNtuple/lowdimuon").Draw("mass >> +hmass_mc", "containstrig > 0.5 && trigger > 1.5 && (genLevel == 4 || genLevel == 5 || genLevel == 6 || genLevel == 7 || genLevel == 8 || genLevel == 9 || genLevel == 10 || genLevel == 11 || genLevel == 12 || genLevel == 13 || genLevel == 14 || genLevel == 15)")
hmass_mc.Scale(hmass.GetEntries() / hmass_mc.GetEntries())
hmass.Fit("background_ansatz4", "LR")
hmass.Fit("background_ansatz4", "LR")
hmass.GetFunction("background_ansatz4").SetLineWidth(3)
hmass.SetAxisRange(0., 95., "Y")
hmass.Draw("e1")
hmass_mc.Draw("same")
scalefake22_fake31 = hmass2.GetEntries() / hmass.GetEntries()
background_fakes = background_ansatz4.Clone()
background_fakes.SetParameters(*[(5.*scalefake22_fake31 if i in (0, 5, 6, 7, 8, 9, 10) else 1.)*hmass.GetFunction("background_ansatz4").GetParameter(i) for i in range(11)])
tlegend = ROOT.TLegend(0.16, 0.75, 0.5, 0.9)
tlegend.SetBorderSize(0); tlegend.SetFillColor(ROOT.kWhite); tlegend.SetTextSize(0.03)
tlegend.AddEntry(hmass, "data: dimuon + 2 extra tracks", "p")
tlegend.AddEntry(hmass.GetFunction("background_ansatz4"), "fit to data", "l")
tlegend.AddEntry(hmass_mc, "MC (decays-in-flight and fakes)", "l")
tlegend.Draw()
c1.SaveAs("FINALPLOTS/backgroundEnriched_fakes.pdf")

########################################################
# control samples

hmask = ROOT.TH1F("hmask", "", 1000, 0.25, 5.)
for i in range(1, 1000+1):
    if abs(hmask.GetBinCenter(i) - 3.096916) < 0.15:
        hmask.SetBinContent(i, 600.)
    else:
        hmask.SetBinContent(i, -0.5)
hmask.SetLineStyle(2)
hmask.SetLineWidth(2)
hmask.SetFillColor(ROOT.kGray)

# set_palette("fireyfire")
# massCFblinded = ROOT.TH2F("massCFblinded", "", 190, 0.25, 5., 190, 0.25, 5.)
# for tfile in inclBB4mu:
#     tfile.Get("FitNtuple/dimudimu").Draw("massC:massF >> +massCFblinded", "containstrig > 0.5 && trigger > 1.5  &&  ((abs(massF - 3.096916) < 0.15  &&  abs(massC - 3.096916) > 0.15) || (abs(massC - 3.096916) < 0.15  &&  abs(massF - 3.096916) > 0.15))")
# massCFblinded.SetYTitle("triggered dimuon mass [GeV/c^{2}]"); massCFblinded.GetYaxis().CenterTitle()
# massCFblinded.SetXTitle("other dimuon mass [GeV/c^{2}]"); massCFblinded.GetXaxis().CenterTitle()
# massCFblinded.Draw("colz")
# tlines = []
# for x1, y1, x2, y2 in [(0.25, 0.25, 3.096916-0.15, 3.096916-0.15),
#                        (3.096916+0.15, 0.25, 5., 3.096916-0.15),
#                        (3.096916+0.15, 3.096916+0.15, 5., 5.),
#                        (0.25, 3.096916+0.15, 3.096916-0.15, 5.),
#                        (3.096916-0.15, 3.096916-0.15, 3.096916+0.15, 3.096916+0.15),
#                        ]:
#     tlines.append(ROOT.TPave(x1, y1, x2, y2))
#     tlines[-1].SetBorderSize(0)
#     tlines[-1].SetFillColor(ROOT.kGray)
#     tlines[-1].Draw()
# for x1, y1, x2, y2 in [(0.25, 3.096916-0.15, 3.096916-0.15, 3.096916-0.15),
#                        (3.096916-0.15, 3.096916-0.15, 3.096916-0.15, 3.096916+0.15),
#                        (3.096916-0.15, 3.096916+0.15, 0.25, 3.096916+0.15),
#                        (3.096916-0.15, 0.25, 3.096916-0.15, 3.096916-0.15),
#                        (3.096916-0.15, 3.096916-0.15, 3.096916+0.15, 3.096916-0.15),
#                        (3.096916+0.15, 3.096916-0.15, 3.096916+0.15, 0.25),
#                        (5., 3.096916-0.15, 3.096916+0.15, 3.096916-0.15),
#                        (3.096916+0.15, 3.096916-0.15, 3.096916+0.15, 3.096916+0.15),
#                        (3.096916+0.15, 3.096916+0.15, 5., 3.096916+0.15),
#                        (3.096916+0.15, 5., 3.096916+0.15, 3.096916+0.15),
#                        (3.096916+0.15, 3.096916+0.15, 3.096916-0.15, 3.096916+0.15),
#                        (3.096916-0.15, 3.096916+0.15, 3.096916-0.15, 5.),
#                        ]:
#     tlines.append(ROOT.TLine(x1, y1, x2, y2))
#     tlines[-1].SetLineStyle(2)
#     tlines[-1].Draw()
# c1.SaveAs("FINALPLOTS/mc_controlregions.pdf")

# massCjpsi = ROOT.TH1F("massCjpsi", "", 190, 0.25, 5.)
# massFjpsi = ROOT.TH1F("massFjpsi", "", 190, 0.25, 5.)
# massC = ROOT.TH1F("massC", "", 190, 0.25, 5.)
# massF = ROOT.TH1F("massF", "", 190, 0.25, 5.)
# for tfile in inclBB4mu:
#     tfile.Get("FitNtuple/dimudimu").Draw("massC >> +massCjpsi", "containstrig > 0.5 && trigger > 1.5  &&  abs(massF - 3.096916) < 0.15  &&  abs(massC - 3.096916) > 0.15")
#     tfile.Get("FitNtuple/dimudimu").Draw("massC >> +massC", "containstrig > 0.5 && trigger > 1.5  &&  abs(massC - 3.096916) > 0.15")
#     tfile.Get("FitNtuple/dimudimu").Draw("massF >> +massFjpsi", "containstrig > 0.5 && trigger > 1.5  &&  abs(massC - 3.096916) < 0.15  &&  abs(massF - 3.096916) > 0.15")
#     tfile.Get("FitNtuple/dimudimu").Draw("massF >> +massF", "containstrig > 0.5 && trigger > 1.5  &&  abs(massF - 3.096916) > 0.15")
# massC.Scale(massCjpsi.GetEntries()/massC.GetEntries())
# massF.Scale(massFjpsi.GetEntries()/massF.GetEntries())
# massC.SetLineColor(ROOT.kRed); massC.SetLineStyle(2); massC.SetLineWidth(2); massCjpsi.SetLineWidth(2)
# massF.SetLineColor(ROOT.kRed); massF.SetLineStyle(2); massF.SetLineWidth(2); massFjpsi.SetLineWidth(2)

# hmask.SetXTitle("triggered dimuon mass [GeV/c^{2}]"); hmask.GetXaxis().CenterTitle()
# hmask.SetYTitle("events per 0.025 GeV/c^{2}"); hmask.GetYaxis().CenterTitle()
# hmask.SetAxisRange(0., 200., "Y")
# hmask.Draw()
# massC.Draw("same")
# massCjpsi.Draw("same")
# tlegend = ROOT.TLegend(0.62, 0.73, 0.82, 0.9)
# tlegend.SetBorderSize(0); tlegend.SetFillColor(ROOT.kWhite); tlegend.SetTextSize(0.03)
# tlegend.AddEntry(hmask, "hidden region", "f")
# tlegend.AddEntry(massCjpsi, "control MC", "l")
# tlegend.AddEntry(massC, "all MC (scaled)", "l")
# tlegend.Draw()
# c1.SaveAs("FINALPLOTS/mc_controlregions_factorize1.pdf")

# hmask.SetXTitle("other dimuon mass [GeV/c^{2}]"); hmask.GetXaxis().CenterTitle()
# hmask.SetYTitle("events per 0.025 GeV/c^{2}"); hmask.GetYaxis().CenterTitle()
# hmask.SetAxisRange(0., 500., "Y")
# hmask.Draw()
# massF.Draw("same")
# massFjpsi.Draw("same")
# tlegend = ROOT.TLegend(0.62, 0.73, 0.82, 0.9)
# tlegend.SetBorderSize(0); tlegend.SetFillColor(ROOT.kWhite); tlegend.SetTextSize(0.03)
# tlegend.AddEntry(hmask, "hidden region", "f")
# tlegend.AddEntry(massCjpsi, "control MC", "l")
# tlegend.AddEntry(massC, "all MC (scaled)", "l")
# tlegend.Draw()
# c1.SaveAs("FINALPLOTS/mc_controlregions_factorize2.pdf")

###

hmask.SetAxisRange(0., 3., "Y")

massCjpsi = ROOT.TH1F("massCjpsi", "", 190, 0.25, 5.)
massFjpsi = ROOT.TH1F("massFjpsi", "", 190, 0.25, 5.)
for tfile in DataSep17 + Data2010B:
    tfile.Get("FitNtuple/dimudimu").Draw("massC >> +massCjpsi", "containstrig > 0.5 && trigger > 1.5  &&  abs(massF - 3.096916) < 0.15  &&  abs(massC - 3.096916) > 0.15")
    tfile.Get("FitNtuple/dimudimu").Draw("massF >> +massFjpsi", "containstrig > 0.5 && trigger > 1.5  &&  abs(massC - 3.096916) < 0.15  &&  abs(massF - 3.096916) > 0.15")
massCjpsi.SetLineWidth(2)
massFjpsi.SetLineWidth(2)
background_dimudimuC.SetLineWidth(2)
background_dimudimuC_50.SetLineWidth(2)
background_dimudimuF.SetLineWidth(2)
background_dimudimuF_50.SetLineWidth(2)

# prediction magnitude = 5.2038132433808508

hmask.SetXTitle("triggered dimuon mass [GeV/c^{2}]"); hmask.GetXaxis().CenterTitle()
hmask.SetYTitle("events per 0.025 GeV/c^{2}"); hmask.GetYaxis().CenterTitle()
hmask.Draw()
massCjpsi.Draw("same")
background_dimudimuC.Draw("same")
background_dimudimuC_50.Draw("same")
tlegend = ROOT.TLegend(0.62, 0.73, 0.82, 0.9)
tlegend.SetBorderSize(0); tlegend.SetFillColor(ROOT.kWhite); tlegend.SetTextSize(0.03)
tlegend.AddEntry(hmask, "hidden region", "f")
tlegend.AddEntry(massCjpsi, "control data", "f")
tlegend.AddEntry(background_dimudimuC, "prediction", "l")
tlegend.AddEntry(background_dimudimuC_50, "prediction #times 50", "l")
tlegend.Draw()
c1.SaveAs("FINALPLOTS/control_massC.pdf")

hmask.SetXTitle("other dimuon mass [GeV/c^{2}]"); hmask.GetXaxis().CenterTitle()
hmask.SetYTitle("events per 0.025 GeV/c^{2}"); hmask.GetYaxis().CenterTitle()
hmask.Draw()
massFjpsi.Draw("same")
background_dimudimuF.Draw("same")
background_dimudimuF_50.Draw("same")
tlegend = ROOT.TLegend(0.62, 0.73, 0.82, 0.9)
tlegend.SetBorderSize(0); tlegend.SetFillColor(ROOT.kWhite); tlegend.SetTextSize(0.03)
tlegend.AddEntry(hmask, "hidden region", "f")
tlegend.AddEntry(massCjpsi, "control data", "f")
tlegend.AddEntry(background_dimudimuC, "prediction", "l")
tlegend.AddEntry(background_dimudimuC_50, "prediction #times 50", "l")
tlegend.Draw()
c1.SaveAs("FINALPLOTS/control_massF.pdf")

###

hmass = ROOT.TH1F("hmass", "", 190, 0.25, 5.); hmass.SetXTitle("mass [GeV/c^{2}]"); hmass.GetXaxis().CenterTitle()
hmass.SetYTitle("events per 0.025 GeV/c^{2}"); hmass.GetYaxis().CenterTitle()
for tfile in DataSep17 + Data2010B:
    tfile.Get("FitNtuple/lowdimuon").Draw("mass >> +hmass", "containstrig > 0.5 && trigger > 1.5 && 60. < pt && pt < 80.")
hmass.SetLineWidth(2)
background_highdimuon.SetLineWidth(3)
hmass.Draw("e1")
background_highdimuon.Draw("same")
tlegend = ROOT.TLegend(0.17, 0.8, 0.5, 0.9)
tlegend.SetBorderSize(0); tlegend.SetFillColor(ROOT.kWhite); tlegend.SetTextSize(0.03)
tlegend.AddEntry(hmass, "data: dimuon 60 < p_{T} < 80 GeV/c", "p")
tlegend.AddEntry(background_highdimuon, "prediction from 40 < p_{T} < 60 GeV/c", "l")
tlegend.Draw()
c1.SaveAs("FINALPLOTS/control_highpt.pdf")

# scale4060_6080 = 0.13893653516295026

###

hmass = ROOT.TH1F("hmass", "", 38, 0.25, 5.); hmass.SetXTitle("mass [GeV/c^{2}]"); hmass.GetXaxis().CenterTitle()
hmass.SetYTitle("events per 0.125 GeV/c^{2}"); hmass.GetYaxis().CenterTitle()
hmass.SetLineWidth(2)
for tfile in DataSep17 + Data2010B:
    tfile.Get("FitNtuple/mujetplustracks").Draw("massa >> +hmass", "containstrig > 0.5 && trigger > 1.5 && muons == 3 && fakes == 1 && charge == 0")
    tfile.Get("FitNtuple/mujetplustracks").Draw("massb >> +hmass", "containstrig > 0.5 && trigger > 1.5 && muons == 3 && fakes == 1 && charge == 0")
hmass.SetLineWidth(3)
hmass.SetMarkerSize(1.5)
background_fakes.SetLineWidth(3)
hmass.SetAxisRange(0., 8., "Y")
hmass.Draw("e1")
background_fakes.Draw("same")
tlegend = ROOT.TLegend(0.17, 0.8, 0.5, 0.9)
tlegend.SetBorderSize(0); tlegend.SetFillColor(ROOT.kWhite); tlegend.SetTextSize(0.03)
tlegend.AddEntry(hmass, "data: trimuon + 1 extra track", "p")
tlegend.AddEntry(background_fakes, "prediction from dimuon + 2 extra tracks", "l")
tlegend.Draw()
c1.SaveAs("FINALPLOTS/control_fakes.pdf")

# scalefake22_fake31 = 0.014437689969604863

#####################################################
# supporting plots

mupt1 = ROOT.TH1F("mupt1", "", 30, 0., 30.)
mupt2 = ROOT.TH1F("mupt2", "", 30, 0., 30.)
mupt3 = ROOT.TH1F("mupt3", "", 30, 0., 30.)
fakept1 = ROOT.TH1F("fakept1", "", 30, 0., 30.)
fakept2 = ROOT.TH1F("fakept2", "", 30, 0., 30.)
for tfile in DataSep17 + Data2010B:
    tfile.Get("FitNtuple/mujetplustracks").Draw("mupt1 >> +mupt1", "containstrig > 0.5 && trigger > 1.5")
    tfile.Get("FitNtuple/mujetplustracks").Draw("mupt2 >> +mupt2", "containstrig > 0.5 && trigger > 1.5")
    tfile.Get("FitNtuple/mujetplustracks").Draw("mupt3 >> +mupt3", "containstrig > 0.5 && trigger > 1.5")
    tfile.Get("FitNtuple/mujetplustracks").Draw("fakept1 >> +fakept1", "containstrig > 0.5 && trigger > 1.5")
    tfile.Get("FitNtuple/mujetplustracks").Draw("fakept2 >> +fakept2", "containstrig > 0.5 && trigger > 1.5")
mupt1.Sumw2()
mupt2.Sumw2()
mupt3.Sumw2()
fakept1.Sumw2()
fakept2.Sumw2()
mupt1.Scale(1./mupt1.Integral())
mupt2.Scale(1./mupt2.Integral())
mupt3.Scale(1./mupt3.Integral())
fakept1.Scale(1./fakept1.Integral())
fakept2.Scale(1./fakept2.Integral())

mupt1.SetMarkerStyle(22); mupt1.SetMarkerColor(ROOT.kBlack); mupt1.SetLineColor(ROOT.kBlack)
mupt2.SetMarkerStyle(23); mupt2.SetMarkerColor(ROOT.kGreen+2); mupt2.SetLineColor(ROOT.kGreen+2)
mupt3.SetMarkerStyle(29); mupt3.SetMarkerColor(ROOT.kMagenta+2); mupt3.SetLineColor(ROOT.kMagenta+2)
fakept1.SetMarkerStyle(24); fakept1.SetMarkerColor(ROOT.kRed); fakept1.SetLineColor(ROOT.kRed)
fakept2.SetMarkerStyle(25); fakept2.SetMarkerColor(ROOT.kBlue); fakept2.SetLineColor(ROOT.kBlue)

mupt1.SetXTitle("p_{T} [GeV/c]")
mupt1.SetYTitle("fraction per GeV/c")
mupt1.GetXaxis().CenterTitle()
mupt1.GetYaxis().CenterTitle()
mupt1.SetAxisRange(0., 0.5, "Y")
mupt1.Draw("e1")
mupt2.Draw("samee1")
mupt3.Draw("samee1")
fakept1.Draw("samee1")
fakept2.Draw("samee1")
tlegend = ROOT.TLegend(0.4, 0.6, 0.75, 0.9)
tlegend.SetBorderSize(0)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetTextSize(0.04)
tlegend.AddEntry(mupt1, "highest muon p_{T}", "p")
tlegend.AddEntry(mupt2, "2^{nd} highest muon p_{T}", "p")
tlegend.AddEntry(mupt3, "3^{rd} highest muon p_{T}", "p")
tlegend.AddEntry(fakept1, "highest added track p_{T}", "p")
tlegend.AddEntry(fakept2, "2^{nd} highest track p_{T}", "p")
tlegend.Draw()
c1.SaveAs("FINALPLOTS/support_mujetplustracks_ptspectra.pdf")

###

def stack(bins, low, high, quantity, cuts, window=None, xtitle=None, ytitle=None, datahist=False, right=False, yoffset=None, tlines=None):
    global hdata, hinclusivemu, hcharmonium1, hcharmonium2, hcharmonium3, hdrellyan, tline, tlegend
    hdata = ROOT.TH1F("hdata", "", bins, low, high)
    hinclusivemu = ROOT.TH1F("hinclusivemu", "", bins, low, high)
    hcharmonium1 = ROOT.TH1F("hcharmonium1", "", bins, low, high)
    hcharmonium2 = ROOT.TH1F("hcharmonium2", "", bins, low, high)
    hcharmonium3 = ROOT.TH1F("hcharmonium3", "", bins, low, high)
    hdrellyan = ROOT.TH1F("hdrellyan", "", bins, low, high)

    for tfile in DataSep17:
        tfile.Get("FitNtuple/lowdimuon").Draw("%s >> +hdata" % quantity, cuts)
    for tfile in Data2010B:
        tfile.Get("FitNtuple/lowdimuon").Draw("%s >> +hdata" % quantity, cuts)
    hdata.Sumw2()

    for tfile in InclusiveMuPt30:
        tfile.Get("FitNtuple/lowdimuon").Draw("%s >> +hinclusivemu" % quantity, cuts)
    hinclusivemu.Sumw2()
    hinclusivemu.Scale(35. / (12.11 * (8873381./9340396.)))

    for tfile in JPsi:
        tfile.Get("FitNtuple/lowdimuon").Draw("%s >> +hcharmonium1" % quantity, cuts)
    hcharmonium1.Sumw2()
    # hcharmonium1.Scale(35. / (13.5 * (7250174./7400174.)))
    hcharmonium1.Scale(35. / (2.*13.5 * (7250174./7400174.)))

    for tfile in Psi2SJPsi:
        tfile.Get("FitNtuple/lowdimuon").Draw("%s >> +hcharmonium2" % quantity, cuts)
    hcharmonium2.Sumw2()
    hcharmonium2.Scale(35. / (69.6 * (1502250./1502250.)))

    for tfile in Psi2S:
        tfile.Get("FitNtuple/lowdimuon").Draw("%s >> +hcharmonium3" % quantity, cuts)
    hcharmonium3.Sumw2()
    hcharmonium3.Scale(35. / (72.0 * (412681./523331.)))

    for tfile in DrellYan:
        tfile.Get("FitNtuple/lowdimuon").Draw("%s >> +hdrellyan" % quantity, cuts)
    hdrellyan.Sumw2()
    # hdrellyan.Scale(0.294)
    hdrellyan.Scale(35. / 65.515)

    hcharmonium1.Add(hinclusivemu)
    hcharmonium2.Add(hcharmonium1)
    hcharmonium3.Add(hcharmonium2)
    hdrellyan.Add(hcharmonium3)

    hdrellyan.SetFillColor(ROOT.kYellow)
    hcharmonium3.SetFillColor(ROOT.kGreen+1)
    hcharmonium2.SetFillColor(ROOT.kGreen+1)
    hcharmonium1.SetFillColor(ROOT.kGreen-9)
    hinclusivemu.SetFillColor(ROOT.kOrange+7)

    if window is not None:
        hdrellyan.SetAxisRange(0., window, "Y")

    if xtitle is not None:
        hdrellyan.SetXTitle(xtitle)
    if ytitle is not None:
        hdrellyan.SetYTitle(ytitle)
    hdrellyan.GetXaxis().CenterTitle()
    hdrellyan.GetYaxis().CenterTitle()
    hdrellyan.GetXaxis().SetTitleSize(0.055)
    # hdrellyan.GetXaxis().SetTitleOffset(1.1)
    hdrellyan.GetYaxis().SetTitleSize(0.055)
    if yoffset is not None:
        hdrellyan.GetYaxis().SetTitleOffset(yoffset)

    if datahist:
        hdata.SetLineColor(ROOT.kBlue)
        hdata.SetLineWidth(2)
    else:
        hdata.SetMarkerSize(0.75)

    hdrellyan.Draw("hist")
    hcharmonium3.Draw("samehist")
    hcharmonium2.Draw("samehist")
    hcharmonium1.Draw("samehist")
    hinclusivemu.Draw("samehist")
    if datahist: hdata.Draw("histsame")
    else: hdata.Draw("e1same")

    if right: move = 0.32
    else: move = 0.

    tline = []
    if tlines is not None and window is not None:
        for t in tlines:
            tline.append(ROOT.TLine(t, 0., t, window))
            tline[-1].SetLineStyle(2)
            tline[-1].Draw()

    tlegend = ROOT.TLegend(0.17 + move, 0.7, 0.45 + move, 0.91)
    tlegend.SetBorderSize(0)
    tlegend.SetFillColor(ROOT.kWhite)
    tlegend.SetTextSize(0.03)
    if datahist: tlegend.AddEntry(hdata, "data (35 pb^{-1})", "l")
    else: tlegend.AddEntry(hdata, "data (35 pb^{-1})", "p")
    tlegend.AddEntry(hinclusivemu, "incl-#mu #hat{p}_{T} > 30 GeV/c MC", "f")
    tlegend.AddEntry(hcharmonium1, "prompt J/#psi and #psi' MC", "f")
    tlegend.AddEntry(hdrellyan, "Drell-Yan MC", "f")
    tlegend.Draw()

stack(190, 0.25, 5., "mass", "containstrig > 0.5 && trigger > 1.5", xtitle="mass [GeV/c^{2}]", ytitle="events per 0.025 GeV/c^{2}", window=400., tlines=[0.5, 1.1, 2.9])
c1.SaveAs("FINALPLOTS/support_mass_all.pdf")

stack(190, 0.25, 5., "mass", "containstrig > 0.5 && trigger > 1.5 && (iso > 4.5 || ((pluspx+minuspx)*vx + (pluspy+minuspy)*vy)/sqrt((pluspx+minuspx)**2 + (pluspy+minuspy)**2) > 0.2)", xtitle="mass with b#bar{b} cuts [GeV/c^{2}]", ytitle="events per 0.025 GeV/c^{2}", window=300., tlines=[0.5, 1.1, 2.9])
c1.SaveAs("FINALPLOTS/support_mass_bbbar.pdf")

stack(190, 0.25, 5., "mass", "containstrig > 0.5 && trigger > 1.5 && !(iso > 4.5 || ((pluspx+minuspx)*vx + (pluspy+minuspy)*vy)/sqrt((pluspx+minuspx)**2 + (pluspy+minuspy)**2) > 0.2)", xtitle="mass with anti-b#bar{b} cuts [GeV/c^{2}]", ytitle="events per 0.025 GeV/c^{2}", window=130., tlines=[0.5, 1.1, 2.9])
c1.SaveAs("FINALPLOTS/support_mass_antibbbar.pdf")

stack(20, 0., 30., "iso", "containstrig > 0.5 && trigger > 1.5", xtitle="Iso [GeV/c]", ytitle="events per 1.5 GeV/c", window=5000., right=True, yoffset=1.2, tlines=[4.5])
c1.SaveAs("FINALPLOTS/support_iso_all.pdf")

stack(20, 0., 30., "iso", "containstrig > 0.5 && trigger > 1.5 && 1.1 < mass && mass < 2.9", xtitle="Iso in continuum [GeV/c]", ytitle="events per 1.5 GeV/c", window=1500., right=True, yoffset=1.2, tlines=[4.5])
c1.SaveAs("FINALPLOTS/support_iso_continuum.pdf")

stack(20, 0., 30., "iso", "containstrig > 0.5 && trigger > 1.5 && 0.35 < mass && mass < 0.5", xtitle="Iso for low-mass [GeV/c]", ytitle="events per 1.5 GeV/c", window=350., right=True, yoffset=1.2, tlines=[4.5])
c1.SaveAs("FINALPLOTS/support_iso_lowmass.pdf")

stack(100, -10., 10., "10.*((pluspx+minuspx)*vx + (pluspy+minuspy)*vy)/sqrt((pluspx+minuspx)**2 + (pluspy+minuspy)**2)", "containstrig > 0.5 && trigger > 1.5", xtitle="L_{xy} [mm]", ytitle="events per 0.2 mm", window=2100., tlines=[2.])
c1.SaveAs("FINALPLOTS/support_lxy_all.pdf")

stack(100, -10., 10., "10.*((pluspx+minuspx)*vx + (pluspy+minuspy)*vy)/sqrt((pluspx+minuspx)**2 + (pluspy+minuspy)**2)", "containstrig > 0.5 && trigger > 1.5 && 1.1 < mass && mass < 2.9", xtitle="L_{xy} in continuum [mm]", ytitle="events per 0.2 mm", window=450., tlines=[2.])
c1.SaveAs("FINALPLOTS/support_lxy_continuum.pdf")

stack(100, -10., 10., "10.*((pluspx+minuspx)*vx + (pluspy+minuspy)*vy)/sqrt((pluspx+minuspx)**2 + (pluspy+minuspy)**2)", "containstrig > 0.5 && trigger > 1.5 && 0.35 < mass && mass < 0.5", xtitle="L_{xy} for low-mass [mm]", ytitle="events per 0.2 mm", window=60., tlines=[2.])
c1.SaveAs("FINALPLOTS/support_lxy_lowmass.pdf")

###

tdrStyle.SetOptFit(111)

hmass = ROOT.TH1F("hmass", "", 190, 0.25, 5.)
hmass_cut = ROOT.TH1F("hmass_cut", "", 190, 0.25, 5.)
hmass_ratio = ROOT.TH1F("hmass_ratio", "", 190, 0.25, 5.)
for tfile in InclusiveMuPt30:
    tfile.Get("FitNtuple/lowdimuon").Draw("mass >> +hmass", "containstrig > 0.5 && trigger > 1.5")
    tfile.Get("FitNtuple/lowdimuon").Draw("mass >> +hmass_cut", "containstrig > 0.5 && trigger > 1.5 && (iso > 4.5 || ((pluspx+minuspx)*vx + (pluspy+minuspy)*vy)/sqrt((pluspx+minuspx)**2 + (pluspy+minuspy)**2) > 0.2)")
for i in range(1, 190+1):
    if hmass.GetBinContent(i) > 0.:
        p = hmass_cut.GetBinContent(i) / hmass.GetBinContent(i)
        hmass_ratio.SetBinContent(i, p)
        hmass_ratio.SetBinError(i, sqrt(p * (1. - p) / hmass.GetBinContent(i)))
    else:
        hmass_ratio.SetBinContent(i, 0.)
        hmass_ratio.SetBinError(i, 0.)
fconst = ROOT.TF1("fconst", "[0]", 0.25, 5.)
hmass_ratio.Fit("fconst", "R")

hmass_ratio.SetLineWidth(2)
hmass_ratio.GetFunction("fconst").SetLineWidth(3)
hmass_ratio.SetXTitle("mass [GeV/c^{2}]")
hmass_ratio.SetYTitle("efficiency of b#bar{b} cut (MC)")
hmass_ratio.GetXaxis().CenterTitle()
hmass_ratio.GetYaxis().CenterTitle()
hmass_ratio.SetAxisRange(0., 1.3, "Y")
hmass_ratio.Draw("e1")
c1.SaveAs("FINALPLOTS/support_bbbarcut_efficiency.pdf")

###

hpt = ROOT.TH1F("hpt_anticut", "", 60, 20., 80.)
hpt_cut = ROOT.TH1F("hpt_cut", "", 60, 20., 80.)
for tfile in DataSep17 + Data2010B:
    tfile.Get("FitNtuple/lowdimuon").Draw("pt >> +hpt_anticut", "containstrig > 0.5 && trigger > 1.5 && !(iso > 4.5 || ((pluspx+minuspx)*vx + (pluspy+minuspy)*vy)/sqrt((pluspx+minuspx)**2 + (pluspy+minuspy)**2) > 0.2)")
    tfile.Get("FitNtuple/lowdimuon").Draw("pt >> +hpt_cut", "containstrig > 0.5 && trigger > 1.5 && (iso > 4.5 || ((pluspx+minuspx)*vx + (pluspy+minuspy)*vy)/sqrt((pluspx+minuspx)**2 + (pluspy+minuspy)**2) > 0.2)")
hpt.Sumw2()
hpt_cut.Sumw2()

hpt.SetAxisRange(5e-1, 8e3, "Y")
hpt.SetXTitle("p_{T} [GeV/c]")
hpt.SetYTitle("events per GeV/c")
hpt.GetXaxis().CenterTitle()
hpt.GetYaxis().CenterTitle()
hpt.GetYaxis().SetTitleOffset(0.9)

hpt.SetLineWidth(2)
hpt_cut.SetLineWidth(2)
hpt.SetMarkerStyle(24)
hpt_cut.SetLineColor(ROOT.kRed); hpt_cut.SetMarkerColor(ROOT.kRed); 

fexpo = ROOT.TF1("fexpo", "[0]*exp(-x/[1])/([1]*(exp(-40./[1]) - exp(-80./[1])))", 40., 80.)
fexpo.SetParNames("A", "k [GeV/c]")
fexpo.SetParameters(2000., 10.)
hpt.Fit("fexpo", "LR")
hpt_cut.Fit("fexpo", "LR")
hpt.GetFunction("fexpo").SetLineWidth(3); hpt.GetFunction("fexpo").SetLineColor(ROOT.kBlack)
hpt_cut.GetFunction("fexpo").SetLineWidth(3)

c1.SetLogy(1)
hpt.Draw("e1")
hpt_cut.Draw("samee1")
tline1 = ROOT.TLine(40., 5e-1, 40., 8e3); tline1.SetLineStyle(2); tline1.Draw()
tline2 = ROOT.TLine(60., 5e-1, 60., 8e3); tline2.SetLineStyle(2); tline2.Draw()
tlegend = ROOT.TLegend(0.17, 0.81, 0.5, 0.9)
tlegend.SetBorderSize(0)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetTextSize(0.03)
tlegend.AddEntry(hpt_cut, "data with b#bar{b} cut", "pl")
tlegend.AddEntry(hpt, "data with b#bar{b} anti-cut", "pl")
tlegend.Draw()
c1.SaveAs("FINALPLOTS/support_bbbarcut_limits.pdf")
c1.SetLogy(0)

####################################################################
# resolutions

hresbarrel = {}
for massrange in [(0., 1.), (1., 2.), (2., 3.), (3., 4.), (4., 5.)]:
    for ptrange in [(20., 30.), (30., 50.), (50., 70.), (70., 100.)]:
        name = "peakbarrel_%g_%g_%g_%g" % (massrange[0], massrange[1], ptrange[0], ptrange[1])
        hresbarrel[name] = ROOT.TH1F(name, "", 200, -0.5, 0.5)
        for tfile in PairGun:
            tfile.Get("FitNtuple/lowdimuon").Draw("mass - genmass >> +%s" % name, "%g < mass && mass < %g && %g < pt && pt < %g && containstrig > 0.5 && trigger > 1.5" % (massrange[0], massrange[1], ptrange[0], ptrange[1]))
        hresbarrel[name].Sumw2()

        # f = ROOT.TF1("f", "[0]*(((exp(-x**2 / 2. / [1]**2) / sqrt(2.*3.1415926) / [1])*(x/[1] > -[2]) + (0.4/[1])*(exp(-[2]**2/2.)/abs([2])/(1./abs([2]) - abs([2]) - x/[1]))*(x/[1] < -[2])))", -0.5, 0.5)
        f = ROOT.TF1("f", "[0]*((1. - [3])*((exp(-x**2 / 2. / [1]**2) / sqrt(2.*3.1415926) / [1])) + [3]*exp(-x**2 / 2. / 0.07**2) / sqrt(2.*3.1415926) / 0.07)", -0.5, 0.5)
        f.SetNpx(800)
        f.SetParameters(hresbarrel[name].GetEntries(), hresbarrel[name].GetRMS(), 1.)
        f.SetParLimits(3, 0., 0.9)

        hresbarrel[name].Fit("f")
        hresbarrel[name].Fit("f")
        hresbarrel[name].Fit("f", "L")
        hresbarrel[name].Fit("f", "L")
        c1.SaveAs("/tmp/whatever/%s.png" % name)

hres = {}
for massrange in [(0., 1.), (1., 2.), (2., 3.), (3., 4.), (4., 5.)]:
    for ptrange in [(10., 30.), (30., 50.), (50., 70.), (70., 100.)]:
        name = "peak_%g_%g_%g_%g" % (massrange[0], massrange[1], ptrange[0], ptrange[1])
        hres[name] = ROOT.TH1F(name, "", 200, -0.5, 0.5)
        for tfile in PairGun:
            tfile.Get("FitNtuple/lowdimuon").Draw("mass - genmass >> +%s" % name, "%g < mass && mass < %g && %g < pt && pt < %g" % (massrange[0], massrange[1], ptrange[0], ptrange[1]))
        hres[name].Sumw2()

        f = ROOT.TF1("f", "[0]*((1. - [3])*((exp(-x**2 / 2. / [1]**2) / sqrt(2.*3.1415926) / [1])) + [3]*exp(-x**2 / 2. / 0.07**2) / sqrt(2.*3.1415926) / 0.07)", -0.5, 0.5)
        f.SetNpx(800)
        f.SetParameters(hres[name].GetEntries(), hres[name].GetRMS(), 1.)
        f.SetParLimits(3, 0., 0.9)

        hres[name].Fit("f")
        hres[name].Fit("f")
        hres[name].Fit("f", "L")
        hres[name].Fit("f", "L")
        c1.SaveAs("/tmp/whatever/%s.png" % name)

hreallylowpt = ROOT.TH1F("hreallylowpt", "", 5, 0., 5.)
hlowpt = ROOT.TH1F("hlowpt", "", 5, 0., 5.)
hmidpt = ROOT.TH1F("hmidpt", "", 5, 0., 5.)
hhighpt = ROOT.TH1F("hhighpt", "", 5, 0., 5.)
hreallylowbarrelpt = ROOT.TH1F("hreallylowbarrelpt", "", 5, 0., 5.)
hlowbarrelpt = ROOT.TH1F("hlowbarrelpt", "", 5, 0., 5.)
hmidbarrelpt = ROOT.TH1F("hmidbarrelpt", "", 5, 0., 5.)
hhighbarrelpt = ROOT.TH1F("hhighbarrelpt", "", 5, 0., 5.)
for i in xrange(1, hreallylowpt.GetNbinsX()+1):
    if i == 1: massrange = (0., 1.)
    elif i == 2: massrange = (1., 2.)
    elif i == 3: massrange = (2., 3.)
    elif i == 4: massrange = (3., 4.)
    elif i == 5: massrange = (4., 5.)
    hreallylowpt.SetBinContent(i, hres["peak_%g_%g_%g_%g" % (massrange[0], massrange[1], 10., 30.)].GetFunction("f").GetParameter(1))
    hlowpt.SetBinContent(i, hres["peak_%g_%g_%g_%g" % (massrange[0], massrange[1], 30., 50.)].GetFunction("f").GetParameter(1))
    hmidpt.SetBinContent(i, hres["peak_%g_%g_%g_%g" % (massrange[0], massrange[1], 50., 70.)].GetFunction("f").GetParameter(1))
    hhighpt.SetBinContent(i, hres["peak_%g_%g_%g_%g" % (massrange[0], massrange[1], 70., 100.)].GetFunction("f").GetParameter(1))
    hreallylowbarrelpt.SetBinContent(i, hresbarrel["peakbarrel_%g_%g_%g_%g" % (massrange[0], massrange[1], 20., 30.)].GetFunction("f").GetParameter(1))
    hlowbarrelpt.SetBinContent(i, hresbarrel["peakbarrel_%g_%g_%g_%g" % (massrange[0], massrange[1], 30., 50.)].GetFunction("f").GetParameter(1))
    hmidbarrelpt.SetBinContent(i, hresbarrel["peakbarrel_%g_%g_%g_%g" % (massrange[0], massrange[1], 50., 70.)].GetFunction("f").GetParameter(1))
    hhighbarrelpt.SetBinContent(i, hresbarrel["peakbarrel_%g_%g_%g_%g" % (massrange[0], massrange[1], 70., 100.)].GetFunction("f").GetParameter(1))

hreallylowptalpha = ROOT.TH1F("hreallylowptalpha", "", 5, 0., 5.)
hlowptalpha = ROOT.TH1F("hlowptalpha", "", 5, 0., 5.)
hmidptalpha = ROOT.TH1F("hmidptalpha", "", 5, 0., 5.)
hhighptalpha = ROOT.TH1F("hhighptalpha", "", 5, 0., 5.)
hreallylowbarrelptalpha = ROOT.TH1F("hreallylowbarrelptalpha", "", 5, 0., 5.)
hlowbarrelptalpha = ROOT.TH1F("hlowbarrelptalpha", "", 5, 0., 5.)
hmidbarrelptalpha = ROOT.TH1F("hmidbarrelptalpha", "", 5, 0., 5.)
hhighbarrelptalpha = ROOT.TH1F("hhighbarrelptalpha", "", 5, 0., 5.)
for i in xrange(1, hreallylowptalpha.GetNbinsX()+1):
    if i == 1: massrange = (0., 1.)
    elif i == 2: massrange = (1., 2.)
    elif i == 3: massrange = (2., 3.)
    elif i == 4: massrange = (3., 4.)
    elif i == 5: massrange = (4., 5.)
    hreallylowptalpha.SetBinContent(i, hres["peak_%g_%g_%g_%g" % (massrange[0], massrange[1], 10., 30.)].GetFunction("f").GetParameter(3))
    hlowptalpha.SetBinContent(i, hres["peak_%g_%g_%g_%g" % (massrange[0], massrange[1], 30., 50.)].GetFunction("f").GetParameter(3))
    hmidptalpha.SetBinContent(i, hres["peak_%g_%g_%g_%g" % (massrange[0], massrange[1], 50., 70.)].GetFunction("f").GetParameter(3))
    hhighptalpha.SetBinContent(i, hres["peak_%g_%g_%g_%g" % (massrange[0], massrange[1], 70., 100.)].GetFunction("f").GetParameter(3))
    hreallylowbarrelptalpha.SetBinContent(i, hresbarrel["peakbarrel_%g_%g_%g_%g" % (massrange[0], massrange[1], 20., 30.)].GetFunction("f").GetParameter(3))
    hlowbarrelptalpha.SetBinContent(i, hresbarrel["peakbarrel_%g_%g_%g_%g" % (massrange[0], massrange[1], 30., 50.)].GetFunction("f").GetParameter(3))
    hmidbarrelptalpha.SetBinContent(i, hresbarrel["peakbarrel_%g_%g_%g_%g" % (massrange[0], massrange[1], 50., 70.)].GetFunction("f").GetParameter(3))
    hhighbarrelptalpha.SetBinContent(i, hresbarrel["peakbarrel_%g_%g_%g_%g" % (massrange[0], massrange[1], 70., 100.)].GetFunction("f").GetParameter(3))

###

hpsiprime = ROOT.TH1F("hpsiprime", "", 50, 3.5, 3.85)
hjpsi = ROOT.TH1F("hjpsi", "", 50, 2.9, 3.25)
hphi = ROOT.TH1F("hphi", "", 50, 0.9, 1.15)
homega = ROOT.TH1F("homega", "", 50, 0.5, 1.0)
for tfile in DataSep17 + Data2010B:
    tfile.Get("FitNtuple/lowdimuon").Draw("mass >> +hpsiprime", "containstrig > 0.5 && trigger > 1.5")
    tfile.Get("FitNtuple/lowdimuon").Draw("mass >> +hjpsi", "containstrig > 0.5 && trigger > 1.5")
    tfile.Get("FitNtuple/lowdimuon").Draw("mass >> +hphi", "containstrig > 0.5 && trigger > 1.5")
    tfile.Get("FitNtuple/lowdimuon").Draw("mass >> +homega", "containstrig > 0.5 && trigger > 1.5")
hpsiprime.Sumw2()
hjpsi.Sumw2()
hphi.Sumw2()
homega.Sumw2()

hjpsi2 = ROOT.TH1F("hjpsi2", "", 50, 2.9, 3.25)
for tfile in DataSep17 + Data2010B:
    tfile.Get("FitNtuple/dimuorphan").Draw("mass >> +hjpsi2", "orphanpt > 15. && abs(orphaneta) < 0.9 && containstrig > 0.5 && trigger > 1.5")
hjpsi2.Sumw2()

bkgnd = ROOT.TF1("bkgnd", "[0] + [1]*x", 0., 4.)
bkgnd.SetLineColor(ROOT.kRed)
bkgnd.SetLineStyle(2)
bkgnd.SetLineWidth(3)

resx = []
resy = []
resyerr = []

fpsiprime = ROOT.TF1("fpsiprime", "[0]*exp(-(x-3.68609)**2 / 2. / [1]**2) / sqrt(2.*3.1415926) / [1] + [2] + [3]*x")
fpsiprime.SetParameters(100., 0.05, 0., 0., 3.5, 3.85)
fpsiprime.SetParNames("p_{#psi'}", "#sigma_{#psi'}", "p_{0}", "p_{1}")
hpsiprime.Fit("fpsiprime", "L")
hpsiprime.SetXTitle("mass [GeV/c^{2}]")
hpsiprime.GetXaxis().CenterTitle()
hpsiprime.SetYTitle("events per 0.007 GeV/c^{2}")
hpsiprime.GetYaxis().CenterTitle()
hpsiprime.SetAxisRange(0., 45., "Y")
hpsiprime.SetLineWidth(2); hpsiprime.GetFunction("fpsiprime").SetLineWidth(3)
hpsiprime.Draw("e1")
bkgnd.SetParameters(hpsiprime.GetFunction("fpsiprime").GetParameter(2), hpsiprime.GetFunction("fpsiprime").GetParameter(3))
bkgnd.Draw("same")
resx.append(3.68609)
resy.append(hpsiprime.GetFunction("fpsiprime").GetParameter(1))
resyerr.append(hpsiprime.GetFunction("fpsiprime").GetParError(1))
c1.SaveAs("FINALPLOTS/respeak_psiprime.pdf")

fjpsi = ROOT.TF1("fjpsi", "[0]*((exp(-(x-3.096916)**2 / 2. / [1]**2) / sqrt(2.*3.1415926) / [1])*((x-3.096916)/[1] > -[2]) + (0.4/[1])*(exp(-[2]**2/2.)/abs([2])/(1./abs([2]) - abs([2]) - (x-3.096916)/[1]))*((x-3.096916)/[1] < -[2])) + [3]", 2.9, 3.25)
fjpsi.SetParameters(100., 0.05, 1., 0.)
fjpsi.SetParNames("p_{J/#psi}", "#sigma_{J/#psi}", "#alpha", "p_{0}")
hjpsi.Fit("fjpsi", "L")
hjpsi.SetXTitle("mass [GeV/c^{2}]")
hjpsi.GetXaxis().CenterTitle()
hjpsi.SetYTitle("events per 0.007 GeV/c^{2}")
hjpsi.GetYaxis().CenterTitle()
hjpsi.SetAxisRange(0., 700., "Y")
hjpsi.SetLineWidth(2); hjpsi.GetFunction("fjpsi").SetLineWidth(3)
hjpsi.Draw("e1")
bkgnd.SetParameters(hjpsi.GetFunction("fjpsi").GetParameter(3), 0.)
bkgnd.Draw("same")
resx.append(3.096916)
resy.append(hjpsi.GetFunction("fjpsi").GetParameter(1))
resyerr.append(hjpsi.GetFunction("fjpsi").GetParError(1))
c1.SaveAs("FINALPLOTS/respeak_jpsi.pdf")

fjpsi2 = ROOT.TF1("fjpsi2", "[0]*(exp(-(x-3.096916)**2 / 2. / [1]**2) / sqrt(2.*3.1415926) / [1]) + [2]", 2.9, 3.25)
fjpsi2.SetParameters(100., 0.05, 1.)
fjpsi2.SetParNames("p'_{J/#psi}", "#sigma'_{J/#psi}", "p_{0}")
hjpsi2.Fit("fjpsi2")
hjpsi2.Fit("fjpsi2")
hjpsi2.Fit("fjpsi2", "L")
hjpsi2.Fit("fjpsi2", "L")
hjpsi2.SetXTitle("mass [GeV/c^{2}]")
hjpsi2.GetXaxis().CenterTitle()
hjpsi2.SetYTitle("events per 0.007 GeV/c^{2}")
hjpsi2.GetYaxis().CenterTitle()
hjpsi2.SetAxisRange(0., 12., "Y")
hjpsi2.SetLineWidth(2); hjpsi2.GetFunction("fjpsi2").SetLineWidth(3)
hjpsi2.Draw("e1")
bkgnd.SetParameters(hjpsi2.GetFunction("fjpsi2").GetParameter(2), 0.)
bkgnd.Draw("same")
resy_jpsi2 = abs(hjpsi2.GetFunction("fjpsi2").GetParameter(1))
resyerr_jpsi2 = hjpsi2.GetFunction("fjpsi2").GetParError(1)
c1.SaveAs("FINALPLOTS/respeak_jpsi2.pdf")

fphi = ROOT.TF1("fphi", "[0]*exp(-(x-1.019455)**2 / 2. / [1]**2) / sqrt(2.*3.1415926) / [1] + [2] + [3]*x", 0.9, 1.15)
fphi.SetParameters(100., 0.01, 0., 0.)
fphi.SetParNames("p_{#phi}", "#sigma_{#phi}", "p_{0}", "p_{1}")
hphi.Fit("fphi", "L")
hphi.SetXTitle("mass [GeV/c^{2}]")
hphi.GetXaxis().CenterTitle()
hphi.SetYTitle("events per 0.005 GeV/c^{2}")
hphi.GetYaxis().CenterTitle()
hphi.SetAxisRange(0., 70., "Y")
hphi.SetLineWidth(2); hphi.GetFunction("fphi").SetLineWidth(3)
hphi.Draw("e1")
bkgnd.SetParameters(hphi.GetFunction("fphi").GetParameter(2), hphi.GetFunction("fphi").GetParameter(3))
bkgnd.Draw("same")
resx.append(1.019455)
resy.append(hphi.GetFunction("fphi").GetParameter(1))
resyerr.append(hphi.GetFunction("fphi").GetParError(1))
c1.SaveAs("FINALPLOTS/respeak_phi.pdf")

fomega = ROOT.TF1("fomega", "[0]*exp(-(x-0.78265)**2 / 2. / [1]**2) / sqrt(2.*3.1415926) / [1] + [2]*exp(-(x-0.77549)**2 / 2. / 0.149**2) / sqrt(2.*3.1415926) / 0.149 + [3] + [4]*x", 0.5, 1.0)
fomega.SetParameters(100., 0.01, 0., 0., 0.)
fomega.SetParNames("p_{#omega}", "#sigma_{#omega}", "p_{#rho}", "p_{0}", "p_{1}")
homega.Fit("fomega")
homega.Fit("fomega")
homega.Fit("fomega", "L")
homega.Fit("fomega", "L")
homega.SetXTitle("mass [GeV/c^{2}]")
homega.GetXaxis().CenterTitle()
homega.SetYTitle("events per 0.01 GeV/c^{2}")
homega.GetYaxis().CenterTitle()
homega.SetAxisRange(0., 140., "Y")
homega.SetLineWidth(2); homega.GetFunction("fomega").SetLineWidth(3)
homega.Draw("e1")
bkgnd.SetParameters(homega.GetFunction("fomega").GetParameter(3), homega.GetFunction("fomega").GetParameter(4))
bkgnd.Draw("same")
resx.append(0.78265)
resy.append(homega.GetFunction("fomega").GetParameter(1))
resyerr.append(homega.GetFunction("fomega").GetParError(1))
c1.SaveAs("FINALPLOTS/respeak_omega.pdf")

###

g = ROOT.TGraphErrors(len(resx), array.array("d", resx), array.array("d", resy), array.array("d", len(resx)*[0.]), array.array("d", resyerr))
g2 = ROOT.TGraph(len(resx), array.array("d", resx), array.array("d", resy))
g3 = ROOT.TGraphErrors(1, array.array("d", [resx[1]]), array.array("d", [resy_jpsi2]), array.array("d", [0.]), array.array("d", [resyerr_jpsi2]))
g4 = ROOT.TGraph(1, array.array("d", [resx[1]]), array.array("d", [resy_jpsi2 - resyerr_jpsi2/2.]))
g5 = ROOT.TGraph(1, array.array("d", [resx[1]]), array.array("d", [resy_jpsi2]))
g6 = ROOT.TGraph(1, array.array("d", [resx[1]]), array.array("d", [resy_jpsi2 + resyerr_jpsi2/2.]))

hreallylowbarrelpt.SetLineColor(ROOT.kBlack)
hlowbarrelpt.SetLineColor(ROOT.kRed)
hmidbarrelpt.SetLineColor(ROOT.kGreen+2)
hhighbarrelpt.SetLineColor(ROOT.kBlue)
hreallylowpt.SetLineColor(ROOT.kBlack)
hlowpt.SetLineColor(ROOT.kRed)
hmidpt.SetLineColor(ROOT.kGreen+2)
hhighpt.SetLineColor(ROOT.kBlue)
hreallylowpt.SetLineStyle(2)
hlowpt.SetLineStyle(2)
hmidpt.SetLineStyle(2)
hhighpt.SetLineStyle(2)

hreallylowbarrelpt.SetXTitle("mass [GeV/c^{2}]")
hreallylowbarrelpt.SetYTitle("#sigma [GeV/c^{2}]")
hreallylowbarrelpt.GetXaxis().CenterTitle()
hreallylowbarrelpt.GetYaxis().CenterTitle()
hreallylowbarrelpt.GetYaxis().SetTitleOffset(1.1)

g.SetLineWidth(2)
g2.SetMarkerColor(ROOT.kWhite)
g2.SetMarkerSize(3.)
g3.SetLineWidth(2)
g3.SetMarkerStyle(25)
g3.SetLineColor(ROOT.kMagenta+2); g3.SetMarkerColor(ROOT.kMagenta+2)
for gg in g4, g5, g6:
    gg.SetMarkerColor(ROOT.kWhite)
    gg.SetMarkerSize(3.)
hreallylowbarrelpt.SetLineWidth(3)
hlowbarrelpt.SetLineWidth(3)
hmidbarrelpt.SetLineWidth(3)
hhighbarrelpt.SetLineWidth(3)
hreallylowpt.SetLineWidth(3)
hlowpt.SetLineWidth(3)
hmidpt.SetLineWidth(3)
hhighpt.SetLineWidth(3)

hreallylowbarrelpt.SetAxisRange(0., 0.09, "Y")
hreallylowbarrelpt.Draw("L")
hlowbarrelpt.Draw("Lsame")
hmidbarrelpt.Draw("Lsame")
hhighbarrelpt.Draw("Lsame")
hreallylowpt.Draw("Lsame")
hlowpt.Draw("Lsame")
hmidpt.Draw("Lsame")
hhighpt.Draw("Lsame")
g4.Draw("p")
g5.Draw("p")
g6.Draw("p")
g2.Draw("p")
g3.Draw("p")
g.Draw("p")
tlegend = ROOT.TLegend(0.17, 0.52-0.05, 0.6, 0.92)
tlegend.SetBorderSize(0)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetTextSize(0.03)
tlegend.AddEntry(g, "resonance fits (data) with triggered muon", "p")
tlegend.AddEntry(g3, "J/#psi fit (data) with no trigger bias", "p")
tlegend.AddEntry(hreallylowbarrelpt, "MC-truth 20 < p_{T} < 30 GeV/c and |#eta| < 0.9", "l")
tlegend.AddEntry(hlowbarrelpt, "MC-truth 30 < p_{T} < 50 GeV/c and |#eta| < 0.9", "l")
tlegend.AddEntry(hmidbarrelpt, "MC-truth 50 < p_{T} < 70 GeV/c and |#eta| < 0.9", "l")
tlegend.AddEntry(hhighbarrelpt, "MC-truth 70 < p_{T} < 100 GeV/c and |#eta| < 0.9", "l")
tlegend.AddEntry(hreallylowpt, "MC-truth 10 < p_{T} < 30 GeV/c and |#eta| < 2.4", "l")
tlegend.AddEntry(hlowpt, "MC-truth 30 < p_{T} < 50 GeV/c and |#eta| < 2.4", "l")
tlegend.AddEntry(hmidpt, "MC-truth 50 < p_{T} < 70 GeV/c and |#eta| < 2.4", "l")
tlegend.AddEntry(hhighpt, "MC-truth 70 < p_{T} < 100 GeV/c and |#eta| < 2.4", "l")
tlegend.Draw()
c1.SaveAs("FINALPLOTS/resolution.pdf")

# f = ROOT.TF1("f", "0.007 + 0.006*x", 0., 5.)  # +0.003
# f.Draw("same")

# f = ROOT.TF1("f", "0.007 + 0.010*x", 0., 5.)
# f.Draw("same")

###

g = ROOT.TGraphErrors(1, array.array("d", [3.096916]), array.array("d", [hjpsi.GetFunction("fjpsi").GetParameter(2)]), array.array("d", [0.]), array.array("d", [hjpsi.GetFunction("fjpsi").GetParError(2)]))
g2 = ROOT.TGraph(1, array.array("d", [3.096916]), array.array("d", [hjpsi.GetFunction("fjpsi").GetParameter(2)]))

hreallylowbarrelptalpha.SetLineColor(ROOT.kBlack)
hlowbarrelptalpha.SetLineColor(ROOT.kRed)
hmidbarrelptalpha.SetLineColor(ROOT.kGreen+2)
hhighbarrelptalpha.SetLineColor(ROOT.kBlue)
hreallylowptalpha.SetLineColor(ROOT.kBlack)
hlowptalpha.SetLineColor(ROOT.kRed)
hmidptalpha.SetLineColor(ROOT.kGreen+2)
hhighptalpha.SetLineColor(ROOT.kBlue)
hreallylowptalpha.SetLineStyle(2)
hlowptalpha.SetLineStyle(2)
hmidptalpha.SetLineStyle(2)
hhighptalpha.SetLineStyle(2)

g.SetLineWidth(2)
g2.SetMarkerColor(ROOT.kWhite)
g2.SetMarkerSize(3.)
hreallylowbarrelptalpha.SetLineWidth(3)
hlowbarrelptalpha.SetLineWidth(3)
hmidbarrelptalpha.SetLineWidth(3)
hhighbarrelptalpha.SetLineWidth(3)
hreallylowptalpha.SetLineWidth(3)
hlowptalpha.SetLineWidth(3)
hmidptalpha.SetLineWidth(3)
hhighptalpha.SetLineWidth(3)

hreallylowbarrelptalpha.SetXTitle("mass [GeV/c^{2}]")
hreallylowbarrelptalpha.SetYTitle("f_{0.07}")
hreallylowbarrelptalpha.GetXaxis().CenterTitle()
hreallylowbarrelptalpha.GetYaxis().CenterTitle()
hreallylowbarrelptalpha.GetYaxis().SetTitleOffset(0.8)

hreallylowbarrelptalpha.SetAxisRange(0., 1., "Y")
hreallylowbarrelptalpha.Draw("L")
hlowbarrelptalpha.Draw("Lsame")
hmidbarrelptalpha.Draw("Lsame")
hhighbarrelptalpha.Draw("Lsame")
hreallylowptalpha.Draw("Lsame")
hlowptalpha.Draw("Lsame")
hmidptalpha.Draw("Lsame")
hhighptalpha.Draw("Lsame")
tlegend = ROOT.TLegend(0.17, 0.52, 0.6, 0.92)
tlegend.SetBorderSize(0)
tlegend.SetFillColor(ROOT.kWhite)
tlegend.SetTextSize(0.03)
tlegend.AddEntry(hreallylowbarrelpt, "MC-truth 20 < p_{T} < 30 GeV/c and |#eta| < 0.9", "l")
tlegend.AddEntry(hlowbarrelpt, "MC-truth 30 < p_{T} < 50 GeV/c and |#eta| < 0.9", "l")
tlegend.AddEntry(hmidbarrelpt, "MC-truth 50 < p_{T} < 70 GeV/c and |#eta| < 0.9", "l")
tlegend.AddEntry(hhighbarrelpt, "MC-truth 70 < p_{T} < 100 GeV/c and |#eta| < 0.9", "l")
tlegend.AddEntry(hreallylowpt, "MC-truth 10 < p_{T} < 30 GeV/c and |#eta| < 2.4", "l")
tlegend.AddEntry(hlowpt, "MC-truth 30 < p_{T} < 50 GeV/c and |#eta| < 2.4", "l")
tlegend.AddEntry(hmidpt, "MC-truth 50 < p_{T} < 70 GeV/c and |#eta| < 2.4", "l")
tlegend.AddEntry(hhighpt, "MC-truth 70 < p_{T} < 100 GeV/c and |#eta| < 2.4", "l")
tlegend.Draw()
c1.SaveAs("FINALPLOTS/resolution_f007.pdf")
