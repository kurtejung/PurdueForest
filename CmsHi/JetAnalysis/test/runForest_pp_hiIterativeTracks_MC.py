import FWCore.ParameterSet.VarParsing as VarParsing

ivars = VarParsing.VarParsing('python')

ivars.register ('randomNumber',
                1,
                ivars.multiplicity.singleton,
                ivars.varType.int,
                "Random Seed")

ivars.register ('secFiles',
                1,
                ivars.multiplicity.singleton,
                ivars.varType.string,
                "Random Seed")

ivars.randomNumber = 1

#ivars.inputFiles = "file:/mnt/hadoop/cms/store/user/dgulhan/pPb/Hijing_Pythia_pt120/RECOv3/reco1_prod1_hijing_fix_277_2_AKa.root"
ivars.inputFiles = "file:prod1_hijing_fix_112_1_iOy.root"
ivars.outputFile = './test_output.root'

ivars.parseArguments()


import FWCore.ParameterSet.Config as cms

process = cms.Process('hiForestAna2011')

process.options = cms.untracked.PSet(
   # wantSummary = cms.untracked.bool(True)
)

genTag="generator"
hltProcess="HLT"

vtxTag="hiSelectedVertex"
trkTag="hiGeneralTracks"
pfTag="particleFlowTmp"

hiTrackQuality = "highPurity"              # iterative tracks

doElectrons = False


#####################################################################################

process.load("CmsHi.JetAnalysis.HiForest_cff")
process.HiForest.inputLines = cms.vstring("HiForest V2 for pPb",
                                          "PF : generalTracks (pp) with highPurity",
                                          "EP Flattening OFF",
                                          "Electrons OFF",
                                          "Preshower OFF"
                                          )

#####################################################################################
# Input source
#####################################################################################

process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                            fileNames = cms.untracked.vstring(ivars.inputFiles),
#                            secondaryFileNames = cms.untracked.vstring(ivars.secFiles),
                            )

# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
            input = cms.untracked.int32(-1))


#####################################################################################
# Load some general stuff
#####################################################################################

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('HLTrigger.Configuration.HLT_PIon_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('RecoLocalTracker.SiPixelRecHits.PixelCPEESProducers_cff')
process.load('PhysicsTools.PatAlgos.patSequences_cff')

#process.load('MitHig.PixelTrackletAnalyzer.pixelHitAnalyzer_cfi')

# Data Global Tag 44x 
#process.GlobalTag.globaltag = 'GR_P_V27::All'

#process.Timing = cms.Service("Timing")

# MC Global Tag 53x 
#process.GlobalTag.globaltag = 'STARTHI53_V17::All'
process.GlobalTag.globaltag = 'STARTHI53_V14::All'

# load centrality
from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import *
overrideGT_pp2760(process)
overrideGT_PbPb2760(process)

process.HeavyIonGlobalParameters = cms.PSet(
    centralityVariable = cms.string("HFtowersPlusTrunc"),
    nonDefaultGlauberModel = cms.string("Hijing"),
    centralitySrc = cms.InputTag("pACentrality")
    )

process.load("CmsHi.JetAnalysis.RandomCones_cff")

process.RandomNumberGeneratorService.generator.initialSeed = ivars.randomNumber 

process.RandomNumberGeneratorService.akPu2PFCones = process.RandomNumberGeneratorService.generator.clone()
process.RandomNumberGeneratorService.akPu3PFCones = process.RandomNumberGeneratorService.generator.clone()
process.RandomNumberGeneratorService.akPu4PFCones = process.RandomNumberGeneratorService.generator.clone()
process.RandomNumberGeneratorService.akPu5PFCones = process.RandomNumberGeneratorService.generator.clone()
process.RandomNumberGeneratorService.akPu6PFCones = process.RandomNumberGeneratorService.generator.clone()

process.RandomNumberGeneratorService.akPu2CaloCones = process.RandomNumberGeneratorService.generator.clone()
process.RandomNumberGeneratorService.akPu3CaloCones = process.RandomNumberGeneratorService.generator.clone()
process.RandomNumberGeneratorService.akPu4CaloCones = process.RandomNumberGeneratorService.generator.clone()
process.RandomNumberGeneratorService.akPu5CaloCones = process.RandomNumberGeneratorService.generator.clone()
process.RandomNumberGeneratorService.akPu6CaloCones = process.RandomNumberGeneratorService.generator.clone()

process.RandomNumberGeneratorService.multiPhotonAnalyzer = process.RandomNumberGeneratorService.generator.clone()

# EcalSeverityLevel ES Producer
process.load("RecoLocalCalo/EcalRecAlgos/EcalSeverityLevelESProducer_cfi")
process.load("RecoEcal.EgammaCoreTools.EcalNextToDeadChannelESProducer_cff")

#####################################################################################
# Define tree output
#####################################################################################

process.TFileService = cms.Service("TFileService",
                                  fileName=cms.string(ivars.outputFile))

#####################################################################################
# Additional Reconstruction and Analysis
#####################################################################################

# MET: Calorimeter based MET
process.load("RecoMET.METProducers.CaloMET_cfi") 

process.load("CmsHi.JetAnalysis.hcalNoise_cff")

# Define Analysis sequencues
process.load('CmsHi.JetAnalysis.EventSelection_cff')
process.load('CmsHi.JetAnalysis.ExtraGenReco_cff')
process.load('CmsHi.JetAnalysis.ExtraTrackReco_cff')
process.load('CmsHi.JetAnalysis.ExtraPfReco_cff')
process.load('CmsHi.JetAnalysis.HiTrackJets_cff')
process.load('CmsHi.JetAnalysis.ExtraJetReco_cff')
process.load('CmsHi.JetAnalysis.ExtraEGammaReco_cff')
process.load('CmsHi.JetAnalysis.PatAna_MC_cff')
process.load('CmsHi.JetAnalysis.JetAnalyzers_MC_cff')
process.load('CmsHi.JetAnalysis.TrkAnalyzers_MC_cff')
process.load('CmsHi.JetAnalysis.EGammaAnalyzers_cff')

process.load("MitHig.PixelTrackletAnalyzer.METAnalyzer_cff")
process.load("CmsHi.JetAnalysis.pfcandAnalyzer_cfi")

process.load('CmsHi.JetAnalysis.rechitanalyzer_cfi')
process.rechitanalyzer.HFTreePtMin = -999
process.rechitanalyzer.HBHETreePtMin = -999
process.rechitanalyzer.EBTreePtMin = -999
process.rechitanalyzer.EBTreePtMin = -999
process.rechitanalyzer.EETreePtMin = -999

process.rechitAna = cms.Sequence(process.rechitanalyzer+process.pfTowers)

process.pfcandAnalyzer.skipCharged = False
process.pfcandAnalyzer.pfPtMin = 0
process.interestingTrackEcalDetIds.TrackCollection = cms.InputTag(trkTag)

process.genpana = cms.EDAnalyzer("GenParticleCounter",
                                 src = cms.untracked.string("hiGenParticles"),
                                 doCentrality = cms.untracked.bool(False),
                                 VertexProducer = cms.untracked.string("hiSelectedVertex")
                                 )

#########################
# Track Analyzer
#########################
process.ppTrack.qualityStrings = cms.untracked.vstring('highPurity','highPuritySetWithPV')
process.ppTrack.trackPtMin = 0.1
process.ppTrack.simTrackPtMin = 0.09
process.pixelTrack = process.ppTrack.clone(trackSrc = cms.InputTag("pixelTracks"),
                                           fillSimTrack = False
                                           )

# Muons 
process.load("MuTrig.HLTMuTree.hltMuTree_cfi")
process.muonTree = process.hltMuTree.clone()
process.muonTree.doGen = cms.untracked.bool(True)

# Event tree
process.load("CmsHi/HiHLTAlgos.hievtanalyzer_cfi")
process.hiEvtAnalyzer.doMC = cms.bool(True)

process.ppTrack.vertexSrc = [vtxTag]

process.iterativeConePu5CaloJets.srcPVs = vtxTag
process.iterativeCone5CaloJets.srcPVs = vtxTag

process.particleFlowTmp.vertexCollection = cms.InputTag(vtxTag)
process.rechitanalyzer.vtxSrc = cms.untracked.InputTag(vtxTag)
process.muonTree.vertices = cms.InputTag(vtxTag)

process.hiEvtAnalyzer.Vertex = cms.InputTag(vtxTag)
process.hiEvtAnalyzer.doEvtPlane = False
process.hiEvtAnalyzer.Centrality = cms.InputTag("pACentrality")

process.primaryVertexFilter.src = cms.InputTag(vtxTag)
process.cleanPhotons.primaryVertexProducer = cms.string(vtxTag)
process.pfTrackElec.PrimaryVertexLabel = cms.InputTag(vtxTag)
process.pfTrack.PrimaryVertexLabel = cms.InputTag(vtxTag)
process.particleFlowTmp.vertexCollection = cms.InputTag(vtxTag)
process.mvaElectrons.vertexTag = cms.InputTag(vtxTag)
process.iterativeConePu5CaloJets.jetPtMin = cms.double(3.0)

process.PFTowers.src = cms.InputTag(pfTag)
process.akPu1PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.akPu2PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.akPu3PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.akPu4PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.akPu5PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.akPu6PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)

process.ak1PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.ak2PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.ak3PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.ak4PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.ak5PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.ak6PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)

process.akPu1CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.akPu2CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.akPu3CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.akPu4CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.akPu5CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.akPu6CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)

process.ak1CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.ak2CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.ak3CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.ak4CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.ak5CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.ak6CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)

process.icPu5JetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.ic5JetAnalyzer.pfCandidateLabel = cms.untracked.InputTag(pfTag)
process.pfcandAnalyzer.pfCandidateLabel = cms.InputTag(pfTag)

process.hiGenParticles.srcVector = [genTag]
process.icPu5JetAnalyzer.eventInfoTag = cms.InputTag(genTag)
process.akPu1PFJetAnalyzer.eventInfoTag = cms.InputTag(genTag)
process.akPu2PFJetAnalyzer.eventInfoTag = cms.InputTag(genTag)
process.akPu3PFJetAnalyzer.eventInfoTag = cms.InputTag(genTag)
process.akPu4PFJetAnalyzer.eventInfoTag = cms.InputTag(genTag)
process.akPu5PFJetAnalyzer.eventInfoTag = cms.InputTag(genTag)
process.akPu6PFJetAnalyzer.eventInfoTag = cms.InputTag(genTag)

process.akPu1CaloJetAnalyzer.eventInfoTag = cms.InputTag(genTag)
process.akPu2CaloJetAnalyzer.eventInfoTag = cms.InputTag(genTag)
process.akPu3CaloJetAnalyzer.eventInfoTag = cms.InputTag(genTag)
process.akPu4CaloJetAnalyzer.eventInfoTag = cms.InputTag(genTag)
process.akPu5CaloJetAnalyzer.eventInfoTag = cms.InputTag(genTag)
process.akPu6CaloJetAnalyzer.eventInfoTag = cms.InputTag(genTag)

process.ak1PFJetAnalyzer.eventInfoTag = cms.InputTag(genTag)
process.ak2PFJetAnalyzer.eventInfoTag = cms.InputTag(genTag)
process.ak3PFJetAnalyzer.eventInfoTag = cms.InputTag(genTag)
process.ak4PFJetAnalyzer.eventInfoTag = cms.InputTag(genTag)
process.ak5PFJetAnalyzer.eventInfoTag = cms.InputTag(genTag)
process.ak6PFJetAnalyzer.eventInfoTag = cms.InputTag(genTag)

process.ak1CaloJetAnalyzer.eventInfoTag = cms.InputTag(genTag)
process.ak2CaloJetAnalyzer.eventInfoTag = cms.InputTag(genTag)
process.ak3CaloJetAnalyzer.eventInfoTag = cms.InputTag(genTag)
process.ak4CaloJetAnalyzer.eventInfoTag = cms.InputTag(genTag)
process.ak5CaloJetAnalyzer.eventInfoTag = cms.InputTag(genTag)
process.ak6CaloJetAnalyzer.eventInfoTag = cms.InputTag(genTag)

process.multiPhotonAnalyzer.GenEventScale = cms.InputTag(genTag)
process.multiPhotonAnalyzer.HepMCProducer = cms.InputTag(genTag)

process.icPu5JetAnalyzer.hltTrgResults = cms.untracked.string('TriggerResults::'+hltProcess)
process.akPu3PFJetAnalyzer.hltTrgResults = cms.untracked.string('TriggerResults::'+hltProcess)
process.heavyIon.generators = cms.vstring("generator")


#Commented by Yen-Jie
#process.hiPixelAdaptiveVertex.useBeamConstraint = False

process.HiGenParticleAna = cms.EDAnalyzer("HiGenAnalyzer")
process.HiGenParticleAna.src= cms.untracked.InputTag("hiGenParticles")
process.HiGenParticleAna.chargedOnly = cms.untracked.bool(False)
process.HiGenParticleAna.ptMin = cms.untracked.double(0)

process.load("RecoHI.HiMuonAlgos.HiRecoMuon_cff")
process.muons.JetExtractorPSet.JetCollectionLabel = cms.InputTag("iterativeConePu5CaloJets")
process.hiTracks.cut = cms.string('quality("' + hiTrackQuality+  '")')

#process.load("edwenger.HiTrkEffAnalyzer.hitrkEffAnalyzer_cff")

process.cutsTPForFak.tracks = cms.untracked.InputTag('TrackingParticles')

#  Following is the reco before adding b-tagging -Matt

###########################################
# Here it is after including b-tagging -Matt

process.pfTrack.TrackQuality = cms.string(hiTrackQuality)

process.hiTracks.src = cms.InputTag(trkTag)
process.hiCaloCompatibleGeneralTracksQuality.src = cms.InputTag(trkTag)
process.hiGeneralTracksQuality.src = cms.InputTag(trkTag)
process.hiSelectedTrackQuality.src = cms.InputTag(trkTag)

process.hitrkEffAnalyzer_akpu3pf.tracks = cms.untracked.InputTag(trkTag)
process.hitrkEffAnalyzer_akpu3pf.vertices = cms.untracked.InputTag(vtxTag)


process.hiTrackReco = cms.Sequence(process.heavyIonTracking * process.hiTracks)
process.hiTrackDebug = cms.Sequence(process.hiSelectedTrackQuality)
process.trackeff_seq = cms.Sequence(process.hitrkEffAnalyzer_akpu3pf)

process.genParticles.src = cms.InputTag(genTag)


#####################################################################################
# PF
#####################################################################################

process.load('CmsHi.JetAnalysis.ExtraPfReco_cff')
process.particleFlowTmp.postMuonCleaning = False
process.particleFlowClusterPS.thresh_Pt_Seed_Endcap = cms.double(99999.)
process.pfTrack.UseQuality = True

process.pfTrack.TkColList = cms.VInputTag("hiGeneralTracks")
process.pfTrack.TrackQuality = cms.string('loose')

process.pfTrack.GsfTracksInEvents = cms.bool(False)
process.HiParticleFlowReco.remove(process.electronsWithPresel)
process.particleFlowTmp.usePFElectrons = cms.bool(False)
process.particleFlowTmp.useEGammaElectrons = cms.bool(False)
process.particleFlowBlock.RecMuons = 'muons'

#####################################################################################
# Extra RECO path
#####################################################################################

process.reco_extra =  cms.Path(
    process.siPixelRecHits*
    process.pACentrality*
    process.hiTrackReco
    +process.hiTrackDebug

    *process.HiParticleFlowLocalReco
    *process.HiParticleFlowReco
    *process.hiGeneralCaloMatchedTracks

    #    process.recoTrackJets*
    *process.recoFastJets    
    *process.iterativeConePu5CaloJets
    *process.PFTowers
    *process.genParticles
    *process.patDefaultSequence
)    
    
#####################################################################################

# seed the muons with iterative tracks
process.globalMuons.TrackerCollectionLabel = "generalTracks"
process.muons.TrackExtractorPSet.inputTrackCollection = "generalTracks"
process.muons.inputCollectionLabels = ["generalTracks", "globalMuons", "standAloneMuons:UpdatedAtVtx", "tevMuons:firstHit", "tevMuons:picky", "tevMuons:dyt"]

# set track collection to iterative tracking
process.pfTrack.TkColList = cms.VInputTag("generalTracks")

# End modifications to reco sequence -Matt
##########################################

process.reco_extra_jet    = cms.Path(process.iterativeConePu5CaloJets *
                                     process.iterativeCone5CaloJets *
                                     process.recoJetsWithID 
#                                     *process.photon_extra_reco
                                     )
process.gen_step          = cms.Path( process.hiGen )

###########################################

process.akPu1PFcorr.payload = 'AK1PF_hiIterativeTracks'
process.akPu2PFcorr.payload = 'AK2PF_hiIterativeTracks'
process.akPu3PFcorr.payload = 'AK3PF_hiIterativeTracks'
process.akPu4PFcorr.payload = 'AK4PF_hiIterativeTracks'
process.akPu5PFcorr.payload = 'AK5PF_hiIterativeTracks'
process.akPu6PFcorr.payload = 'AK6PF_hiIterativeTracks'

process.ak1PFcorr.payload = 'AK1PF_hiIterativeTracks'
process.ak2PFcorr.payload = 'AK2PF_hiIterativeTracks'
process.ak3PFcorr.payload = 'AK3PF_hiIterativeTracks'
process.ak4PFcorr.payload = 'AK4PF_hiIterativeTracks'
process.ak5PFcorr.payload = 'AK5PF_hiIterativeTracks'
process.ak6PFcorr.payload = 'AK6PF_hiIterativeTracks'

###########################################                                                                                                   


process.pat_step          = cms.Path(process.makeHeavyIonJets
#                                     +
#                                     process.makeHeavyIonPhotons
                                     )

    
process.pat_step.remove(process.interestingTrackEcalDetIds)
process.photonMatch.matched = cms.InputTag("hiGenParticles")

process.patPhotons.addPhotonID = cms.bool(False)

#process.extrapatstep = cms.Path(process.selectedPatPhotons)

process.multiPhotonAnalyzer.GammaEtaMax = cms.untracked.double(100)
process.multiPhotonAnalyzer.GammaPtMin = cms.untracked.double(10)
process.multiPhotonAnalyzer.PhotonProducer = cms.InputTag("selectedPatPhotons")
process.multiPhotonAnalyzer.TrackProducer = cms.InputTag("generalTracks")
process.multiPhotonAnalyzer.basicClusterBarrel = cms.InputTag("hybridSuperClusters:hybridBarrelBasicClusters")
process.multiPhotonAnalyzer.basicClusterEndcap = cms.InputTag("multi5x5SuperClusters:multi5x5EndcapBasicClusters")

process.ana_step          = cms.Path(process.fastjet +                                     
                                     process.genpana +
                                      process.hcalNoise +
                                      process.jetAnalyzers +                                      
                                      process.multiPhotonAnalyzer +
                                      process.HiGenParticleAna +
                                      process.cutsTPForFak +
                                      process.cutsTPForEff +
                                      process.trackeff_seq+
                                      process.anaTrack +
                                      process.pixelTrack +
                                      process.pfcandAnalyzer +
                                      process.rechitAna +
                                      process.met * process.anaMET +
				      process.muonTree +
				      process.hiEvtAnalyzer +
                                      process.randomCones +
                                      process.HiForest
                                      )


process.hfPosFilter2 = cms.EDFilter("CandCountFilter",
                                      src = cms.InputTag("hfPosTowers"),
                                      minNumber = cms.uint32(2)
                                      )

process.hfNegFilter2 = cms.EDFilter("CandCountFilter",
                                    src = cms.InputTag("hfNegTowers"),
                                      minNumber = cms.uint32(2)
                                    )

process.pcollisionEventSelection = cms.Path(process.collisionEventSelection)
process.pPAcollisionEventSelectionPA = cms.Path(process.PAcollisionEventSelection)

process.pHBHENoiseFilter = cms.Path( process.HBHENoiseFilter )
process.phiEcalRecHitSpikeFilter = cms.Path(process.hiEcalRecHitSpikeFilter )

process.phfPosFilter3 = cms.Path(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter3)
process.phfNegFilter3 = cms.Path(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfNegFilter3)
process.phfPosFilter2 = cms.Path(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter2)
process.phfNegFilter2 = cms.Path(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfNegFilter2)
process.phfPosFilter1 = cms.Path(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfPosFilter)
process.phfNegFilter1 = cms.Path(process.towersAboveThreshold+process.hfPosTowers+process.hfNegTowers+process.hfNegFilter)
process.phltPixelClusterShapeFilter = cms.Path(process.siPixelRecHits+process.hltPixelClusterShapeFilter)
process.pprimaryvertexFilter = cms.Path(process.primaryVertexFilter)
process.pBeamScrapingFilter=cms.Path(process.NoScraping)
process.pVertexFilterCutG = cms.Path(process.pileupVertexFilterCutG)
process.pVertexFilterCutGloose = cms.Path(process.pileupVertexFilterCutGloose)
process.pVertexFilterCutGtight = cms.Path(process.pileupVertexFilterCutGtight)
process.pVertexFilterCutGplus = cms.Path(process.pileupVertexFilterCutGplus)
process.pVertexFilterCutE = cms.Path(process.pileupVertexFilterCutE)
process.pVertexFilterCutEandG = cms.Path(process.pileupVertexFilterCutEandG)
 

# Customization
from CmsHi.JetAnalysis.customise_cfi import *
setPhotonObject(process,"photons")

from PhysicsTools.PatAlgos.tools.coreTools import *

removeSpecificPATObjects(process,names=['Jets', 'METs'],outputModules =[])
removeMCMatching(process,['Photons'],outputModules =[])
process.patDefaultSequence.remove(process.cleanPatJets)

process.load('L1Trigger.Configuration.L1Extra_cff')
process.load('CmsHi.HiHLTAlgos.hltanalysis_cff')

process.hltanalysis.hltresults = cms.InputTag("TriggerResults","",hltProcess)
process.hltanalysis.HLTProcessName = hltProcess
process.hltanalysis.dummyBranches = []

process.hltAna = cms.EndPath(process.hltanalysis)
process.reco_extra*=process.L1Extra

process.pAna = cms.EndPath(process.skimanalysis)
process.endjob_step = cms.EndPath(process.endOfProcess)

#process.schedule = process.HLTSchedule
#process.postHLTschedule = cms.Schedule(
process.schedule = cms.Schedule(
    process.HLT_PAZeroBiasPixel_SingleTrack_v1,
    process.reco_extra, process.reco_extra_jet, process.gen_step, process.pat_step,
#                                process.extrapatstep,
                                process.ana_step,
    process.pcollisionEventSelection,process.pHBHENoiseFilter,process.phiEcalRecHitSpikeFilter,
    process.pPAcollisionEventSelectionPA,
    process.phfPosFilter3,process.phfNegFilter3,
    process.phfPosFilter2,process.phfNegFilter2,
    process.phfPosFilter1,process.phfNegFilter1,
    process.phltPixelClusterShapeFilter,process.pprimaryvertexFilter,
    process.pBeamScrapingFilter,    
    process.pVertexFilterCutG,
    process.pVertexFilterCutGloose,
    process.pVertexFilterCutGtight,
    process.pVertexFilterCutGplus,
    process.pVertexFilterCutE,
    process.pVertexFilterCutEandG,    
    process.hltAna,process.pAna
    )

#process.schedule.extend(process.postHLTschedule)


########### random number seed

#####################################################################################
# Edm Output
#####################################################################################

#process.out = cms.OutputModule("PoolOutputModule",
#                               fileName = cms.untracked.string("output.root")
#                               )
#process.save = cms.EndPath(process.out)
