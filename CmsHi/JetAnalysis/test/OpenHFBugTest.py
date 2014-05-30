import FWCore.ParameterSet.VarParsing as VarParsing

import FWCore.ParameterSet.Config as cms

process = cms.Process('hiForestAna2011')

vtxTag="offlinePrimaryVertices"
trkTag="generalTracks"

hiTrackQuality = "highPurity"              # iterative tracks

miniForest = True

doCrash = True

#####################################################################################
# Input source
#####################################################################################

process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                            fileNames = cms.untracked.vstring("file:/usr/rmt_share/scratch95/j/jung68/pPb_tempTest/D43CAAE9-3D66-E211-A43F-0025901D624E.root")
                            )

# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
            input = cms.untracked.int32(10))


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
#process.load('HLTrigger.Configuration.HLT_PIon_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')

process.GlobalTag.globaltag = 'GR_P_V43D::All'

# load centrality
from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import *
overrideGT_pPb5020(process)

process.HeavyIonGlobalParameters = cms.PSet(
  centralityVariable = cms.string("HFtowersPlusTrunc"),
  nonDefaultGlauberModel = cms.string(""),
  centralitySrc = cms.InputTag("pACentrality"),
  pPbRunFlip = cms.untracked.uint32(211313)
  )
        
# EcalSeverityLevel ES Producer
process.load("RecoLocalCalo/EcalRecAlgos/EcalSeverityLevelESProducer_cfi")
process.load("RecoEcal.EgammaCoreTools.EcalNextToDeadChannelESProducer_cff")

#####################################################################################
# Define tree output
#####################################################################################

process.TFileService = cms.Service("TFileService",
                                  fileName=cms.string("hiHFBugOutput.root"))

#####################################################################################
# Additional Reconstruction and Analysis
#####################################################################################

#OpenHF Additional Loads
process.load("CondCore.DBCommon.CondDBCommon_cfi")
process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.load("UserCode.OpenHF.HFHiForestSync_cff")

# Define Analysis sequencues
process.load('CmsHi.JetAnalysis.EventSelection_cff')
process.load('CmsHi.JetAnalysis.ExtraGenReco_cff')
process.load('CmsHi.JetAnalysis.ExtraTrackReco_cff')
process.load('CmsHi.JetAnalysis.ExtraPfReco_cff')
process.load('CmsHi.JetAnalysis.HiTrackJets_cff')
process.load('CmsHi.JetAnalysis.ExtraJetReco_cff')

#########################
#########################

process.iterativeConePu5CaloJets.srcPVs = vtxTag
process.iterativeCone5CaloJets.srcPVs = vtxTag

process.particleFlowTmp.vertexCollection = cms.InputTag(vtxTag)

process.primaryVertexFilter.src = cms.InputTag(vtxTag)
process.cleanPhotons.primaryVertexProducer = cms.string(vtxTag)
process.pfTrackElec.PrimaryVertexLabel = cms.InputTag(vtxTag)
process.pfTrack.PrimaryVertexLabel = cms.InputTag(vtxTag)
process.particleFlowTmp.vertexCollection = cms.InputTag(vtxTag)
process.mvaElectrons.vertexTag = cms.InputTag(vtxTag)

process.hiTracks.cut = cms.string('quality("' + hiTrackQuality+  '")')

#  Following is the reco before adding b-tagging -Matt

###########################################
# Here it is after including b-tagging -Matt

process.pfTrack.TrackQuality = cms.string(hiTrackQuality)

process.hiTracks.src = cms.InputTag(trkTag)
process.hiCaloCompatibleGeneralTracksQuality.src = cms.InputTag(trkTag)
process.hiGeneralTracksQuality.src = cms.InputTag(trkTag)
process.hiSelectedTrackQuality.src = cms.InputTag(trkTag)

process.hiTrackReco = cms.Sequence(process.hiTracks)
process.hiTrackDebug = cms.Sequence(process.hiSelectedTrackQuality)
process.PFTowers.src = cms.InputTag("particleFlow")

process.reco_extra =  cms.Path(
    process.siPixelRecHits*
    process.pACentrality* ##vulnerable
    process.hiTrackReco*
    process.recoFastJets*
    process.iterativeConePu5CaloJets* ##vulnerable
    process.PFTowers ##vulnerable
)    

#=======

process.HFTree = cms.EDAnalyzer(
        "HFTree",
        verbose      = cms.untracked.int32(1),
        printFrequency = cms.untracked.int32(100),
        requireCand  =  cms.untracked.bool(True)
        )

process.HFTree_step = cms.Path (process.OpenHfTree)

process.endjob_step = cms.EndPath(process.endOfProcess)

#######====================

if doCrash:
    process.schedule = cms.Schedule(
        process.reco_extra,
        process.HFTree_step,
        process.endjob_step
        )
else:
    process.schedule = cms.Schedule(
            process.HFTree_step,
            process.reco_extra,
            process.endjob_step
            )

