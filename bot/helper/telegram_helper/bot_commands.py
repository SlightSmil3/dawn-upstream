from bot import CMD_INDEX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f'start{CMD_INDEX}'
        self.MirrorCommand = f'mirror{CMD_INDEX}'
        self.UnzipMirrorCommand = f'unzipmirror{CMD_INDEX}'
        self.ZipMirrorCommand = f'zipmirror{CMD_INDEX}'
        self.CancelMirror = f'cancel{CMD_INDEX}'
        self.CancelAllCommand = f'cancelall{CMD_INDEX}'
        self.ListCommand = f'list{CMD_INDEX}'
        self.SearchCommand = f'search{CMD_INDEX}'
        self.StatusCommand = f'status{CMD_INDEX}'
        self.AuthorizedUsersCommand = f'users{CMD_INDEX}'
        self.AuthorizeCommand = f'authorize{CMD_INDEX}'
        self.UnAuthorizeCommand = f'unauthorize{CMD_INDEX}'
        self.AddSudoCommand = f'addsudo{CMD_INDEX}'
        self.RmSudoCommand = f'rmsudo{CMD_INDEX}'
        self.PingCommand = f'ping{CMD_INDEX}'
        self.RestartCommand = f'restart{CMD_INDEX}'
        self.StatsCommand = f'stats{CMD_INDEX}'
        self.HelpCommand = f'help{CMD_INDEX}'
        self.LogCommand = f'log{CMD_INDEX}'
        self.CloneCommand = f'clone{CMD_INDEX}'
        self.CountCommand = f'count{CMD_INDEX}'
        self.WatchCommand = f'watch{CMD_INDEX}'
        self.ZipWatchCommand = f'zipwatch{CMD_INDEX}'
        self.QbMirrorCommand = f'qbmirror{CMD_INDEX}'
        self.QbUnzipMirrorCommand = f'qbunzipmirror{CMD_INDEX}'
        self.QbZipMirrorCommand = f'qbzipmirror{CMD_INDEX}'
        self.DeleteCommand = f'del{CMD_INDEX}'
        self.ShellCommand = f'shell{CMD_INDEX}'
        self.ExecHelpCommand = f'exechelp{CMD_INDEX}'
        self.LeechSetCommand = f'leechsetxyz{CMD_INDEX}'
        self.SetThumbCommand = f'setthumbxyz{CMD_INDEX}'
        self.LeechCommand = f'leechxyz{CMD_INDEX}'
        self.UnzipLeechCommand = f'unzipleechxyz{CMD_INDEX}'
        self.ZipLeechCommand = f'zipleechxyz{CMD_INDEX}'
        self.QbLeechCommand = f'qbleechxyz{CMD_INDEX}'
        self.QbUnzipLeechCommand = f'qbunzipleechxyz{CMD_INDEX}'
        self.QbZipLeechCommand = f'qbzipleechxyz{CMD_INDEX}'
        self.LeechWatchCommand = f'leechwatchxyz{CMD_INDEX}'
        self.LeechZipWatchCommand = f'leechzipwatchxyz{CMD_INDEX}'
        self.BtSelectCommand = f'btsel{CMD_INDEX}'
        self.RssListCommand = f'rsslist{CMD_INDEX}'
        self.RssGetCommand = f'rssget{CMD_INDEX}'
        self.RssSubCommand = f'rsssub{CMD_INDEX}'
        self.RssUnSubCommand = f'rssunsub{CMD_INDEX}'
        self.RssSettingsCommand = f'rssset{CMD_INDEX}'
        self.EvalCommand = f'eval{CMD_INDEX}'
        self.ExecCommand = f'exec{CMD_INDEX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_INDEX}'
        self.SleepCommand = f'sleep{CMD_INDEX}'


BotCommands = _BotCommands()
