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

ivars.inputFiles = "file:/afs/cern.ch/work/k/kjung/EADD935E-D595-E211-AF23-848F69FD2943.root"
ivars.outputFile = 'hiForestTreeMC.root'

ivars.parseArguments()


import FWCore.ParameterSet.Config as cms

process = cms.Process('hiForestAna2011')

process.options = cms.untracked.PSet(
    #wantSummary = cms.untracked.bool(True)
)

genTag="generator"
hltProcess="HLT"

vtxTag="offlinePrimaryVertices"
trkTag="generalTracks"

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
            input = cms.untracked.int32(200))


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
process.GlobalTag.globaltag = 'STARTHI53_V17::All'

# load centrality
from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import *
#overrideGT_pPb5020(process)
#overrideCentrality(process)
overrideGT_pp2760(process)

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
process.ppTrack.doSimVertex = False
process.ppTrack.doSimTrack = False
process.ppTrack.fillSimTrack = False
process.pixelTrack = process.ppTrack.clone(trackSrc = cms.InputTag("pixelTracks"),
                                           fillSimTrack = True
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

process.akPu3PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.akPu3PFJetAnalyzer.useMatch = cms.untracked.bool(False)
process.akPu3PFJetAnalyzer.doLifeTimeTagging = cms.untracked.bool(True)

#process.akPu4PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.akPu5PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.akPu5PFJetAnalyzer.useMatch = cms.untracked.bool(False)
process.akPu5PFJetAnalyzer.doLifeTimeTagging = cms.untracked.bool(True)
process.akPu5PFJetAnalyzer.ImpactParameterTagInfos = cms.untracked.string("akPu5PFImpactParameterTagInfos");
process.akPu5PFJetAnalyzer.TrackCountingHighEffBJetTags = cms.untracked.string("akPu5PFTrackCountingHighEffBJetTags");
process.akPu5PFJetAnalyzer.NegativeTrackCountingHighEffJetTags = cms.untracked.string("akPu5PFNegativeTrackCountingHighEffJetTags");
process.akPu5PFJetAnalyzer.TrackCountingHighPurBJetTags = cms.untracked.string("akPu5PFTrackCountingHighPurBJetTags");
process.akPu5PFJetAnalyzer.NegativeTrackCountingHighPur = cms.untracked.string("akPu5PFNegativeTrackCountingHighPur");
process.akPu5PFJetAnalyzer.JetProbabilityBJetTags = cms.untracked.string("akPu5PFJetProbabilityBJetTags");
process.akPu5PFJetAnalyzer.PositiveOnlyJetProbabilityJetTags = cms.untracked.string("akPu5PFPositiveOnlyJetProbabilityJetTags");
process.akPu5PFJetAnalyzer.NegativeOnlyJetProbabilityJetTags = cms.untracked.string("akPu5PFNegativeOnlyJetProbabilityJetTags");
process.akPu5PFJetAnalyzer.JetBProbabilityBJetTags = cms.untracked.string("akPu5PFJetBProbabilityBJetTags");
process.akPu5PFJetAnalyzer.NegativeOnlyJetBProbabilityJetTags = cms.untracked.string("akPu5PFNegativeOnlyJetBProbabilityJetTags");
process.akPu5PFJetAnalyzer.PositiveOnlyJetBProbabilityJetTags = cms.untracked.string("akPu5PFPositiveOnlyJetBProbabilityJetTags");
process.akPu5PFJetAnalyzer.SecondaryVertexTagInfos = cms.untracked.string("akPu5PFSecondaryVertexTagInfos");
process.akPu5PFJetAnalyzer.SecondaryVertexNegativeTagInfos = cms.untracked.string("akPu5PFSecondaryVertexNegativeTagInfos");
process.akPu5PFJetAnalyzer.SimpleSecondaryVertexHighEffBJetTags = cms.untracked.string("akPu5PFSimpleSecondaryVertexHighEffBJetTags");
process.akPu5PFJetAnalyzer.SimpleSecondaryVertexNegativeHighEffBJetTags = cms.untracked.string("akPu5PFSimpleSecondaryVertexNegativeHighEffBJetTags");
process.akPu5PFJetAnalyzer.SimpleSecondaryVertexHighPurBJetTags = cms.untracked.string("akPu5PFSimpleSecondaryVertexHighPurBJetTags");
process.akPu5PFJetAnalyzer.SimpleSecondaryVertexNegativeHighPurBJetTags = cms.untracked.string("akPu5PFSimpleSecondaryVertexNegativeHighPurBJetTags");
process.akPu5PFJetAnalyzer.CombinedSecondaryVertexBJetTags = cms.untracked.string("akPu5PFCombinedSecondaryVertexBJetTags");
process.akPu5PFJetAnalyzer.CombinedSecondaryVertexNegativeBJetTags = cms.untracked.string("akPu5PFCombinedSecondaryVertexNegativeBJetTags");
process.akPu5PFJetAnalyzer.CombinedSecondaryVertexPositiveBJetTags = cms.untracked.string("akPu5PFCombinedSecondaryVertexPositiveBJetTags");
process.akPu5PFJetAnalyzer.NegativeSoftMuonByPtBJetTags = cms.untracked.string("akPu5PFNegativeSoftMuonByPtBJetTags");
process.akPu5PFJetAnalyzer.PositiveSoftMuonByPtBJetTags = cms.untracked.string("akPu5PFPositiveSoftMuonByPtBJetTags");

process.ak5PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.ak5PFJetAnalyzer.useMatch = cms.untracked.bool(False)
process.ak5PFJetAnalyzer.doLifeTimeTagging = cms.untracked.bool(True)
process.ak5PFJetAnalyzer.ImpactParameterTagInfos = cms.untracked.string("ak5PFImpactParameterTagInfos");
process.ak5PFJetAnalyzer.TrackCountingHighEffBJetTags = cms.untracked.string("ak5PFTrackCountingHighEffBJetTags");
process.ak5PFJetAnalyzer.NegativeTrackCountingHighEffJetTags = cms.untracked.string("ak5PFNegativeTrackCountingHighEffJetTags");
process.ak5PFJetAnalyzer.TrackCountingHighPurBJetTags = cms.untracked.string("ak5PFTrackCountingHighPurBJetTags");
process.ak5PFJetAnalyzer.NegativeTrackCountingHighPur = cms.untracked.string("ak5PFNegativeTrackCountingHighPur");
process.ak5PFJetAnalyzer.JetProbabilityBJetTags = cms.untracked.string("ak5PFJetProbabilityBJetTags");
process.ak5PFJetAnalyzer.PositiveOnlyJetProbabilityJetTags = cms.untracked.string("ak5PFPositiveOnlyJetProbabilityJetTags");
process.ak5PFJetAnalyzer.NegativeOnlyJetProbabilityJetTags = cms.untracked.string("ak5PFNegativeOnlyJetProbabilityJetTags");
process.ak5PFJetAnalyzer.JetBProbabilityBJetTags = cms.untracked.string("ak5PFJetBProbabilityBJetTags");
process.ak5PFJetAnalyzer.NegativeOnlyJetBProbabilityJetTags = cms.untracked.string("ak5PFNegativeOnlyJetBProbabilityJetTags");
process.ak5PFJetAnalyzer.PositiveOnlyJetBProbabilityJetTags = cms.untracked.string("ak5PFPositiveOnlyJetBProbabilityJetTags");
process.ak5PFJetAnalyzer.SecondaryVertexTagInfos = cms.untracked.string("ak5PFSecondaryVertexTagInfos");
process.ak5PFJetAnalyzer.SecondaryVertexNegativeTagInfos = cms.untracked.string("ak5PFSecondaryVertexNegativeTagInfos");
process.ak5PFJetAnalyzer.SimpleSecondaryVertexHighEffBJetTags = cms.untracked.string("ak5PFSimpleSecondaryVertexHighEffBJetTags");
process.ak5PFJetAnalyzer.SimpleSecondaryVertexNegativeHighEffBJetTags = cms.untracked.string("ak5PFSimpleSecondaryVertexNegativeHighEffBJetTags");
process.ak5PFJetAnalyzer.SimpleSecondaryVertexHighPurBJetTags = cms.untracked.string("ak5PFSimpleSecondaryVertexHighPurBJetTags");
process.ak5PFJetAnalyzer.SimpleSecondaryVertexNegativeHighPurBJetTags = cms.untracked.string("ak5PFSimpleSecondaryVertexNegativeHighPurBJetTags");
process.ak5PFJetAnalyzer.CombinedSecondaryVertexBJetTags = cms.untracked.string("ak5PFCombinedSecondaryVertexBJetTags");
process.ak5PFJetAnalyzer.CombinedSecondaryVertexNegativeBJetTags = cms.untracked.string("ak5PFCombinedSecondaryVertexNegativeBJetTags");
process.ak5PFJetAnalyzer.CombinedSecondaryVertexPositiveBJetTags = cms.untracked.string("ak5PFCombinedSecondaryVertexPositiveBJetTags");
process.ak5PFJetAnalyzer.NegativeSoftMuonByPtBJetTags = cms.untracked.string("ak5PFNegativeSoftMuonByPtBJetTags");
process.ak5PFJetAnalyzer.PositiveSoftMuonByPtBJetTags = cms.untracked.string("ak5PFPositiveSoftMuonByPtBJetTags");

process.ak3PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.ak3PFJetAnalyzer.useMatch = cms.untracked.bool(False)
process.ak3PFJetAnalyzer.doLifeTimeTagging = cms.untracked.bool(True)
process.ak3PFJetAnalyzer.ImpactParameterTagInfos = cms.untracked.string("ak3PFImpactParameterTagInfos");
process.ak3PFJetAnalyzer.TrackCountingHighEffBJetTags = cms.untracked.string("ak3PFTrackCountingHighEffBJetTags");
process.ak3PFJetAnalyzer.NegativeTrackCountingHighEffJetTags = cms.untracked.string("ak3PFNegativeTrackCountingHighEffJetTags");
process.ak3PFJetAnalyzer.TrackCountingHighPurBJetTags = cms.untracked.string("ak3PFTrackCountingHighPurBJetTags");
process.ak3PFJetAnalyzer.NegativeTrackCountingHighPur = cms.untracked.string("ak3PFNegativeTrackCountingHighPur");
process.ak3PFJetAnalyzer.JetProbabilityBJetTags = cms.untracked.string("ak3PFJetProbabilityBJetTags");
process.ak3PFJetAnalyzer.PositiveOnlyJetProbabilityJetTags = cms.untracked.string("ak3PFPositiveOnlyJetProbabilityJetTags");
process.ak3PFJetAnalyzer.NegativeOnlyJetProbabilityJetTags = cms.untracked.string("ak3PFNegativeOnlyJetProbabilityJetTags");
process.ak3PFJetAnalyzer.JetBProbabilityBJetTags = cms.untracked.string("ak3PFJetBProbabilityBJetTags");
process.ak3PFJetAnalyzer.NegativeOnlyJetBProbabilityJetTags = cms.untracked.string("ak3PFNegativeOnlyJetBProbabilityJetTags");
process.ak3PFJetAnalyzer.PositiveOnlyJetBProbabilityJetTags = cms.untracked.string("ak3PFPositiveOnlyJetBProbabilityJetTags");
process.ak3PFJetAnalyzer.SecondaryVertexTagInfos = cms.untracked.string("ak3PFSecondaryVertexTagInfos");
process.ak3PFJetAnalyzer.SecondaryVertexNegativeTagInfos = cms.untracked.string("ak3PFSecondaryVertexNegativeTagInfos");
process.ak3PFJetAnalyzer.SimpleSecondaryVertexHighEffBJetTags = cms.untracked.string("ak3PFSimpleSecondaryVertexHighEffBJetTags");
process.ak3PFJetAnalyzer.SimpleSecondaryVertexNegativeHighEffBJetTags = cms.untracked.string("ak3PFSimpleSecondaryVertexNegativeHighEffBJetTags");
process.ak3PFJetAnalyzer.SimpleSecondaryVertexHighPurBJetTags = cms.untracked.string("ak3PFSimpleSecondaryVertexHighPurBJetTags");
process.ak3PFJetAnalyzer.SimpleSecondaryVertexNegativeHighPurBJetTags = cms.untracked.string("ak3PFSimpleSecondaryVertexNegativeHighPurBJetTags");
process.ak3PFJetAnalyzer.CombinedSecondaryVertexBJetTags = cms.untracked.string("ak3PFCombinedSecondaryVertexBJetTags");
process.ak3PFJetAnalyzer.CombinedSecondaryVertexNegativeBJetTags = cms.untracked.string("ak3PFCombinedSecondaryVertexNegativeBJetTags");
process.ak3PFJetAnalyzer.CombinedSecondaryVertexPositiveBJetTags = cms.untracked.string("ak3PFCombinedSecondaryVertexPositiveBJetTags");
process.ak3PFJetAnalyzer.NegativeSoftMuonByPtBJetTags = cms.untracked.string("ak3PFNegativeSoftMuonByPtBJetTags");
process.ak3PFJetAnalyzer.PositiveSoftMuonByPtBJetTags = cms.untracked.string("ak3PFPositiveSoftMuonByPtBJetTags");


process.PFTowers.src = cms.InputTag("particleFlow")
process.akPu1PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.akPu2PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.akPu3PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.akPu4PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.akPu5PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.akPu6PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")

process.ak1PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.ak2PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.ak3PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.ak4PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.ak5PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.ak6PFJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")

process.akPu1CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.akPu2CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.akPu3CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.akPu4CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.akPu5CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.akPu6CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")

process.ak1CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.ak2CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.ak3CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.ak4CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.ak5CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.ak6CaloJetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")

process.icPu5JetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.ic5JetAnalyzer.pfCandidateLabel = cms.untracked.InputTag("particleFlow")
process.pfcandAnalyzer.pfCandidateLabel = cms.InputTag("particleFlow")

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


process.hiTrackReco = cms.Sequence(process.hiTracks)
process.hiTrackDebug = cms.Sequence(process.hiSelectedTrackQuality)
process.trackeff_seq = cms.Sequence(process.hitrkEffAnalyzer_akpu3pf)

process.genParticles.src = cms.InputTag(genTag)

process.reco_extra =  cms.Path(
    process.siPixelRecHits*
    process.pACentrality*
    process.hiTrackReco
    +process.hiTrackDebug
    #    process.recoTrackJets*
    *process.recoFastJets    
    *process.iterativeConePu5CaloJets
    *process.PFTowers
    *process.genParticles
    *process.patDefaultSequence
)    
    

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


process.pat_step          = cms.Path(process.makeHeavyIonJets2to5
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
                                      process.jetAnalyzers3to5 +                                      
                                      process.multiPhotonAnalyzer +
                                      #process.HiGenParticleAna +
				      #process.cutsTPForFak +
                                      #process.cutsTPForEff +
                                      #process.trackeff_seq+
                                      process.ppTrack +
                                      process.pixelTrack +
                                      process.pfcandAnalyzer +
                                      process.rechitAna +
                                      process.met * process.anaMET +
				      process.muonTree +
				      process.hiEvtAnalyzer +
                                      #process.randomCones +
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
process.pVertexFilterCutGplusUpsPP = cms.Path(process.pileupVertexFilterCutGplusUpsPP)


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
    #process.HLT_PAZeroBiasPixel_SingleTrack_v1,
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
    process.pVertexFilterCutGplusUpsPP,
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
